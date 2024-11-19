from pydantic import BaseModel
from typing import List, Optional
from crewai import LLM

class SuccessStory(BaseModel):
    short_description: str
    url: str
    company: str
    integrator: Optional[List[str]] = []
    software_manufacturer: Optional[List[str]] = []    
    valid: bool
    feedback: str

class SuccessStoriesList(BaseModel):
    stories: List[SuccessStory]

INPUT_VARIABLES = { 
        "stories_number":2,
        "technology":"Artificial Intelligence",
        "process_scope":"Manufacturing process",
        "company_sector":"pharmaceutical",
        "company_country":"Any"
}

llm = LLM(
    model="gpt-4o-mini",
    temperature=0
)