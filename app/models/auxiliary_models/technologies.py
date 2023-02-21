from typing import Optional, List

from app.models.custom_base_model import CustomBaseModel


class Technologies(CustomBaseModel):
    programming_language: Optional[List[str]] = []
    frameworks: Optional[List[str]] = []
    platforms: Optional[List[str]] = []
    databases: Optional[List[str]] = []

    @staticmethod
    def get_schema():
        return {
            "programming_language": list,
            "frameworks": list,
            "platforms": list,
            "databases": list,
        }
