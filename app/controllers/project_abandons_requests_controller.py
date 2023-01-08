from fastapi import HTTPException

from app.models.project_abandons_request import ProjectAbandonsRequests


class ProjectAbandonsRequestsController:
    @staticmethod
    def post(repository, project_abandonment_request: ProjectAbandonsRequests):
        project_abandonment_request.complete()
        ok = repository.insert(project_abandonment_request)
        if not ok:
            raise HTTPException(status_code=500, detail="Error saving")
        return project_abandonment_request

    @staticmethod
    def get(repository, pid=None, par_id=None, tid=None):
        result = repository.get(pid=pid, par_id=par_id, tid=tid)
        if len(result) == 0 and par_id is not None:
            raise HTTPException(
                status_code=404, detail="Project abandons requests not found"
            )

        if par_id is not None:
            return result[0]
        return result
