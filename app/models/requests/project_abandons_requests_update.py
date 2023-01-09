from json import loads
from typing import Optional

from pydantic import BaseModel

from app.models.auxiliary_models.request_states import RequestStates


class ProjectAbandonsRequestsUpdate(BaseModel):
    par_id: Optional[str]
    state: Optional[RequestStates]
    updated_date: Optional[str] = ""

    def to_json(self):
        return loads(self.json(exclude_defaults=True))
