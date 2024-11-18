#!/usr/bin/env python
from random import randint

from pydantic import BaseModel
from typing import List, Optional

from crewai.flow.flow import Flow, listen, start
from .config import SuccessStoryReqInfo, SuccessStory,SuccessStoryList
from .crews.research_crew.research_crew import ResearchCrew 



class SuccessStoryFlow(Flow[SuccessStoryReqInfo]):

    @start()
    def research_sources(self):
        return ResearchCrew().crew().kickoff(self.state).pydantic #CORREGIR LO QUE SE LE PASA


def kickoff():
    context_variables = SuccessStoryReqInfo(
        stories_number=2,
        technology="Artificial Intelligence",
        process_scope="Manufacturing process",
        company_sector="Automotion",
        company_country="Spain"
    )
    print(context_variables.model_dump())
    stories_flow = SuccessStoryFlow()
    stories_flow.kickoff(context_variables)


def plot():
    stories_flow = SuccessStoryFlow()
    stories_flow.plot()


if __name__ == "__main__":
    
    kickoff()
