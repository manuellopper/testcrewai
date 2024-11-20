#!/usr/bin/env python
from langtrace_python_sdk import langtrace
import os
langtrace.init(api_key=os.getenv('LANGTRACE_API_KEY'))

from pydantic import BaseModel
from typing import List, Optional
import json


from crewai.flow.flow import Flow, listen, start, router
from .config import INPUT_VARIABLES, SuccessStoriesList
from .crews.research_crew.research_crew import ResearchCrew 
from .crews.validation_crew.validation_crew import ValidationCrew 




class SuccessStoryFlow(Flow):

    input_variables = INPUT_VARIABLES
    stories_list = SuccessStoriesList()

    context_variables = {
        **INPUT_VARIABLES,
        "stories": [story.model_dump() for story in stories_list.stories]
    }
    

    @start("invalid_stories")
    def research_sources(self):
        print("##Start of research sources\n")
        result=ResearchCrew().crew().kickoff(self.context_variables).pydantic                 
        print("##End of research sources\n") 
        self.context_variables["stories"] = [story.model_dump() for story in result.stories]
        
        print(json.dumps(self.context_variables["stories"], indent=2))
        
              
        
        
          

    @router(research_sources)
    def router_stories_validation(self):

        print("##Start router\n") 
        print(json.dumps(self.context_variables["stories"], indent=2))
        result=ValidationCrew().crew().kickoff(self.context_variables).pydantic
        self.context_variables["stories"] = [story.model_dump() for story in result.stories]
        print("##End validation \n") 
        print(json.dumps(self.context_variables["stories"], indent=2))
        valid = all(story['valid'] for story in self.context_variables["stories"])
        
        if valid:
            return "valid_stories"
        else:
            return "invalid_stories"
    
    @listen("valid_stories")
    def present_output(self):
        print(json.dumps(self.context_variables["stories"], indent=2))
       
        with open('success_stories.json', 'w') as f:
            json.dump(self.context_variables["stories"], f, indent=2)



def kickoff():
    
      
    stories_flow = SuccessStoryFlow()
    stories_flow.kickoff()


def plot():
    stories_flow = SuccessStoryFlow()
    stories_flow.plot()


if __name__ == "__main__":
    
    kickoff()
