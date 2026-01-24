from pydantic import BaseModel
from typing import Optional

class GrantCreate(BaseModel):
    title: str
    organization: str
    url: str
    deadline: Optional[str] = None
