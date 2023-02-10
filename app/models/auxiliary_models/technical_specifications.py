from typing import Optional, List

from app.models.custom_base_model import CustomBaseModel


class TechnicalSpecifications(CustomBaseModel):
    cloud_providers: Optional[List[str]] = []
    databases: Optional[List[str]] = []

    @staticmethod
    def get_schema():
        return {"cloud_providers": list, "databases": list}
