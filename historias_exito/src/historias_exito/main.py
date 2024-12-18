#!/usr/bin/env python
from pydantic import BaseModel
from typing import List, Optional

from crewai.flow.flow import Flow, listen, start
from .config import CONTEXT_VARIABLES
from .crews.research_crew.research_crew import ResearchCrew 



class SuccessStoryFlow(Flow):

    input_variables = CONTEXT_VARIABLES

    @start()
    def research_sources(self):
        result=ResearchCrew().crew().kickoff(self.input_variables).pydantic #CORREGIR LO QUE SE LE PASA
        print(result)
        #return 


def kickoff():
    
      
    stories_flow = SuccessStoryFlow()
    stories_flow.kickoff()


def plot():
    stories_flow = SuccessStoryFlow()
    stories_flow.plot()


if __name__ == "__main__":
    
    kickoff()
