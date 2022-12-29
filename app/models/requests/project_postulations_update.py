import uuid
from json import loads
from typing import Optional, List

from pydantic import BaseModel

from app.models.states import States


class ProjectPostulationsUpdate(BaseModel):
    ppid: Optional[str]
    state: Optional[States]
    updated_date: Optional[str] = ""

    def to_json(self):
        return loads(self.json(exclude_defaults=True))
