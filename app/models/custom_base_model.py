import uuid
from json import loads

from pydantic.main import BaseModel


class CustomBaseModel(BaseModel):
    @staticmethod
    def get_id():
        myuuid = uuid.uuid4()
        return str(myuuid)

    def to_json(self):
        return loads(self.json(exclude_defaults=True))
