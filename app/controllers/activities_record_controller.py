from fastapi import HTTPException

from app.models.auxiliary_models.activities_record import ActivitiesRecord


class ActivitiesRecordController:
    @staticmethod
    def post(repository, activity: ActivitiesRecord):
        activity.complete()
        ok = repository.insert(activity)
        if not ok:
            raise HTTPException(status_code=500, detail="Error saving")
        return activity

    @staticmethod
    def get(repository, pid=None, action=None):
        result = repository.get(pid=pid, action=action)
        return result
