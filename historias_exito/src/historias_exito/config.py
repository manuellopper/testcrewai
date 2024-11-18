from pydantic import BaseModel
from typing import List, Optional
from crewai import LLM



class SuccessStoryReqInfo(BaseModel):
    stories_number: int
    technology: str
    process_scope: str
    company_sector: str
    company_country: str


class SuccessStory(BaseModel):
    short_description: str
    url: Optional[str]
    company: str
    integrator: Optional[List[str]] = []
    software_manufacturer: Optional[List[str]] = []
    full_article: Optional[str]
    valid: bool

class SuccessStoryList(BaseModel):
    stories: List[SuccessStory]

CONTEXT_VARIABLES = { 
        "stories_number":2,
        "technology":"Artificial Intelligence",
        "process_scope":"Manufacturing process",
        "company_sector":"pharmaceutical",
        "company_country":"Any"
}

llm = LLM(
    model="gpt-4-mini",
    temperature=0
)