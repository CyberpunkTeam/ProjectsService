from typing import Optional, List

from app.models.custom_base_model import CustomBaseModel


class Description(CustomBaseModel):
    files_attached: Optional[dict] = []
    functional_requirements: Optional[List[str]] = []
    non_function_requirements: Optional[List[str]] = []
    summary: Optional[str] = ""

    @staticmethod
    def get_schema():
        return {
            "files_attached": dict,
            "functional_requirements": list,
            "non_function_requirements": list,
            "summary": str,
        }
