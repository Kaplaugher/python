from pydantic import BaseModel
from typing import Optional, List
from datetime import date

class File(BaseModel):
    name: str
    content: str  # This could be a file path or base64 encoded content

class Opportunity(BaseModel):
    id: Optional[int] = None
    name: str
    description: str
    client: str
    date: date
    files: List[str] = []