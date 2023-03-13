from datetime import datetime

from fastapi import HTTPException

from app.controllers.activities_record_controller import ActivitiesRecordController
from app.models.auxiliary_models.actions import Actions
from app.models.auxiliary_models.activities_record import ActivitiesRecord
from app.models.auxiliary_models.project_states import ProjectStates
from app.models.projects import Projects


class ProjectsController:
    @staticmethod
    def post(repository, auxiliary_repository, project: Projects):
        project.complete()
        ok = repository.insert(project)
        if not ok:
            raise HTTPException(status_code=500, detail="Error saving")

        activity = ActivitiesRecord(action=Actions.CREATED, pid=project.pid)
        activity.complete()
        activity = ActivitiesRecordController.post(auxiliary_repository, activity)

        project.activities_record.append(activity)
        return project

    @staticmethod
    def get(
        repository,
        auxiliary_repository,
        pid=None,
        creator_uid=None,
        state=None,
        currency=None,
        min_budget=None,
        max_budget=None,
        project_types=None,
        idioms=None,
        programming_languages=None,
        frameworks=None,
        platforms=None,
        databases=None,
    ):

        result = repository.get(
            pid=pid,
            creator_uid=creator_uid,
            state=state,
            programming_language=programming_languages,
            frameworks=frameworks,
            platforms=platforms,
            databases=databases,
            budget_currency=currency,
            min_tentative_budget=min_budget,
            max_tentative_budget=max_budget,
            idioms=idioms,
            projects_types=project_types,
        )
        if len(result) == 0 and pid is not None:
            raise HTTPException(status_code=404, detail="Project not found")

        if pid is not None:
            project_to_return = result[0]
            activities = ActivitiesRecordController.get(auxiliary_repository, pid)
            project_to_return.activities_record = activities
            return project_to_return
        return result[::-1]

    @staticmethod
    def put(repository, auxiliary_repository, pid, project_update):
        project = ProjectsController.get(repository, auxiliary_repository, pid)

        if (
            project_update.state == ProjectStates.FINISHED
            and project.state != ProjectStates.FINISHED
        ):
            activity = ActivitiesRecord(action=Actions.FINISHED, pid=pid)
            ActivitiesRecordController.post(auxiliary_repository, activity)

        elif (
            project_update.state == ProjectStates.CANCELLED
            and project.state != ProjectStates.CANCELLED
        ):
            activity = ActivitiesRecord(action=Actions.CANCELLED, pid=pid)
            ActivitiesRecordController.post(auxiliary_repository, activity)
        elif project_update.state == ProjectStates.ABANDONS_REQUEST:
            activity = ActivitiesRecord(action=Actions.ABANDONS_REQUEST, pid=pid)
            ActivitiesRecordController.post(auxiliary_repository, activity)
        elif project_update.state == ProjectStates.FINISH_REQUEST:
            activity = ActivitiesRecord(action=Actions.FINISH_REQUEST, pid=pid)
            ActivitiesRecordController.post(auxiliary_repository, activity)

        project_update.pid = pid
        local = datetime.now()
        project_update.updated_date = local.strftime("%d-%m-%Y:%H:%M:%S")
        ok = repository.put(project_update)
        if not ok:
            raise HTTPException(status_code=500, detail="Error to update")

        return ProjectsController.get(repository, auxiliary_repository, pid=pid)
