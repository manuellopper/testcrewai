#!/usr/bin/env python
from pydantic import BaseModel
from typing import List, Optional

from crewai.flow.flow import Flow, listen, start
from .config import CONTEXT_VARIABLES
from .crews.research_crew.research_crew import ResearchCrew 
from .crews.validation_crew.validation_crew import ValidationCrew 


class SuccessStoryFlow(Flow):

    input_variables = CONTEXT_VARIABLES

    @start("invalid_stories")
    def research_sources(self):
        result=ResearchCrew().crew().kickoff(self.input_variables)
        print(result)
        return result

   

    @router(research_sources)
    def router_stories_validation(self, stories_researched):

        valid = True
        if valid:
            return "valid_stories"
        else:
            return "invalid_stories"
    
    @listen("valid_stories")
    def present_output(self):
        pass



def kickoff():
    
      
    stories_flow = SuccessStoryFlow()
    stories_flow.kickoff()


def plot():
    stories_flow = SuccessStoryFlow()
    stories_flow.plot()


if __name__ == "__main__":
    
    kickoff()
