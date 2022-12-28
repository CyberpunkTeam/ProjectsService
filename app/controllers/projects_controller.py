from datetime import datetime

from fastapi import HTTPException
from app.models.projects import Projects


class ProjectsController:
    @staticmethod
    def post(repository, project: Projects):
        project.complete()
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

    @staticmethod
    def put(repository, pid, project_update):
        project_update.pid = pid
        local = datetime.now()
        project_update.updated_date = local.strftime("%d-%m-%Y:%H:%M:%S")
        ok = repository.put(project_update)
        if not ok:
            raise HTTPException(status_code=500, detail="Error to update")

        return ProjectsController.get(repository, pid=pid)
