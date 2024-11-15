#!/usr/bin/env python
from random import randint

from pydantic import BaseModel

from crewai.flow.flow import Flow, listen, start

#from .crews.poem_crew.poem_crew import PoemCrew --->>>> CAMBIAR

class SuccessStoryInfo(BaseModel):
    stories_number: int
    technology: str
    process_scope: str
    company_sector: str
    company_country: str

class SuccessStoryFlow(Flow[SuccessStoryInfo]):

    @start()
    def research_sources(self):
        #first fuction content

    

def kickoff(start_info):
    
    stories_flow = SuccessStoryFlow()
    stories_flow.kickoff(start_info)


def plot():
    stories_flow = SuccessStoryFlow()
    stories_flow.plot()


if __name__ == "__main__":
    context_variables = SuccessStoryInfo(
        stories_number=2,
        technology="Artificial Intelligence",
        process_scope="Manufacturing process",
        company_sector="Automotion",
        company_country="Spain"
    )
    kickoff(context_variables)
