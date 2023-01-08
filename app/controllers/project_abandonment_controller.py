from fastapi import HTTPException

from app.models.project_abandonment import ProjectAbandonment


class ProjectAbandonmentController:
    @staticmethod
    def post(repository, project_abandonment: ProjectAbandonment):
        project_abandonment.complete()
        ok = repository.insert(project_abandonment)
        if not ok:
            raise HTTPException(status_code=500, detail="Error saving")
        return project_abandonment

    @staticmethod
    def get(repository, pid=None, pa_id=None, tid=None):
        result = repository.get(pid=pid, pa_id=pa_id, tid=tid)
        if len(result) == 0 and pa_id is not None:
            raise HTTPException(status_code=404, detail="Project abandonment not found")

        if pa_id is not None:
            return result[0]
        return result
