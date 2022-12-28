import uuid
from json import loads
from typing import Optional, List

from pydantic import BaseModel


class ProjectsUpdate(BaseModel):
    pid: Optional[str] = None
    name: Optional[str] = None
    idioms: Optional[List[str]] = None
    description: Optional[str] = None
    technologies: Optional[List[str]] = None
    updated_date: Optional[str] = ""

    def to_json(self):
        return loads(self.json(exclude_defaults=True))
