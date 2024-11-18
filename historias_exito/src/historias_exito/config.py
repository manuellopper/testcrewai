from pydantic import BaseModel
from typing import List, Optional


class SuccessStoryReqInfo(BaseModel):
    stories_number: int
    technology: str
    process_scope: str
    company_sector: str
    company_country: str


class SuccessStory(BaseModel):
    short_description: str
    url: str
    company: str
    integrator: Optional[List[str]] = []
    software_manufacturer: Optional[List[str]] = []
    full_article: str
    valid: bool

class SuccessStoryList(BaseModel):
    stories: List[SuccessStory]

class SuccessStoryFlow(Flow[SuccessStoryReqInfo]):