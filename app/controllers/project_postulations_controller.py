from datetime import datetime

from fastapi import HTTPException

from app.models.project_postulations import ProjectPostulations


class ProjectPostulationsController:
    @staticmethod
    def post(repository, project_postulation: ProjectPostulations):
        project_postulation.complete()
        ok = repository.insert(project_postulation)
        if not ok:
            raise HTTPException(status_code=500, detail="Error saving")
        return project_postulation

    @staticmethod
    def get(repository, pid=None, tid=None, ppid=None, state=None):
        result = repository.get(pid=pid, tid=tid, ppid=ppid, state=state)
        if len(result) == 0 and ppid is not None:
            raise HTTPException(status_code=404, detail="Project postulation not found")

        if ppid is not None:
            return result[0]
        return result

    @staticmethod
    def put(repository, ppid, project_postulation_update):
        project_postulation_update.ppid = ppid
        local = datetime.now()
        project_postulation_update.updated_date = local.strftime("%d-%m-%Y:%H:%M:%S")
        ok = repository.put(project_postulation_update)
        if not ok:
            raise HTTPException(status_code=500, detail="Error to update")

        return ProjectPostulationsController.get(repository, ppid=ppid)
