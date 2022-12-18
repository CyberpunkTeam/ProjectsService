from fastapi import HTTPException
from app.models.projects import Projects


class ProjectsController:
    @staticmethod
    def post(repository, project: Projects):
        project.pid = project.get_pid()
        ok = repository.insert(project)
        if not ok:
            raise HTTPException(status_code=500, detail="Error saving")
        return project

    @staticmethod
    def get(repository, pid=None, creator_uid=None):
        result = repository.get(pid=pid, creator_uid=creator_uid)
        if len(result) == 0 and pid is not None:
            raise HTTPException(status_code=404, detail="Project not found")

        if pid is not None:
            return result[0]
        return result
