from fastapi import HTTPException

from app.models.project_finished_requests import ProjectFinishedRequests


class ProjectFinishedRequestsController:
    @staticmethod
    def post(repository, project_finished_request: ProjectFinishedRequests):
        project_finished_request.complete()
        ok = repository.insert(project_finished_request)
        if not ok:
            raise HTTPException(status_code=500, detail="Error saving")
        return project_finished_request

    @staticmethod
    def get(repository, pid=None, pfr_id=None, tid=None):
        result = repository.get(pid=pid, pfr_id=pfr_id, tid=tid)
        if len(result) == 0 and pfr_id is not None:
            raise HTTPException(
                status_code=404, detail="Project finished requests not found"
            )

        if pfr_id is not None:
            return result[0]
        return result
