#!/usr/bin/env python
from pydantic import BaseModel
from typing import List, Optional
import json

from crewai.flow.flow import Flow, listen, start
from .config import INPUT_VARIABLES, SuccessStoriesList
from .crews.research_crew.research_crew import ResearchCrew 
from .crews.validation_crew.validation_crew import ValidationCrew 


class SuccessStoryFlow(Flow):

    input_variables = INPUT_VARIABLES
    lista_historias = SuccessStoriesList(stories=[])

    context_variables = {
        **INPUT_VARIABLES,
        "success_stories": json.loads(lista_historias.model_dump_json())
    }
    

    @start("invalid_stories")
    def research_sources(self):
        result=ResearchCrew().crew().kickoff(self.context_variables).pydantic # IMPORTANTE!! Hay que definir salida pydantic de SuccessStoriesList
        self.context_variables["success_stories"] = json.loads(result.model_dump_json())
        
          

    @router(research_sources)
    def router_stories_validation(self):

        valid = True
        if valid:
            return "valid_stories"
        else:
            return "invalid_stories"
    
    @listen("valid_stories")
    def present_output(self):
        print(json.dumps(self.context_variables["success_stories"], indent=2))
        with open('success_stories.json', 'w') as f:
            json.dump(self.context_variables["success_stories"], f, indent=2)



def kickoff():
    
      
    stories_flow = SuccessStoryFlow()
    stories_flow.kickoff()


def plot():
    stories_flow = SuccessStoryFlow()
    stories_flow.plot()


if __name__ == "__main__":
    
    kickoff()
