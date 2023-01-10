from json import loads
from typing import Optional, List

from pydantic import BaseModel

from app.models.auxiliary_models.project_states import ProjectStates


class ProjectsUpdate(BaseModel):
    pid: Optional[str] = None
    name: Optional[str] = None
    idioms: Optional[List[str]] = None
    description: Optional[str] = None
    technologies: Optional[List[str]] = None
    updated_date: Optional[str] = ""
    state: Optional[ProjectStates]
    team_assigned: Optional[str] = None

    def to_json(self):
        return loads(self.json(exclude_defaults=True))
