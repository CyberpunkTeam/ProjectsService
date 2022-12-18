import uuid
from json import loads
from typing import Optional, List

from pydantic import BaseModel


class Projects(BaseModel):
    pid: Optional[str] = None
    name: str
    idioms: List[str]
    description: str
    technologies: List[str]
    creator_uid: str

    def to_json(self):
        return loads(self.json(exclude_defaults=True))

    @staticmethod
    def get_schema():
        return {
            "pid": str,
            "name": str,
            "idioms": list,
            "description": str,
            "technologies": list,
            "creator_uid": str,
        }

    @staticmethod
    def get_pid():
        myuuid = uuid.uuid4()
        return str(myuuid)
