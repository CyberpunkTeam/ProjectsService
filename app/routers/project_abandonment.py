import os
from typing import List

from fastapi import APIRouter

from app import config
from . import auxiliary_repository
from .projects import projects_repository
from ..controllers.activities_record_controller import ActivitiesRecordController
from ..controllers.project_abandonment_controller import ProjectAbandonmentController
from ..controllers.projects_controller import ProjectsController
from ..models.auxiliary_models.actions import Actions
from ..models.auxiliary_models.activities_record import ActivitiesRecord
from ..models.auxiliary_models.project_states import ProjectStates
from ..models.project_abandonment import ProjectAbandonment
from ..models.requests.project_update import ProjectsUpdate
from ..repositories.project_abandonment_repository import ProjectAbandonmentRepository

router = APIRouter()

# Repository
project_abandonment_repository = ProjectAbandonmentRepository(
    config.DATABASE_URL, config.DATABASE_NAME
)


@router.post(
    "/project_abandonment/reset", tags=["project_abandonment"], status_code=200
)
async def reset():
    if os.environ.get("TEST_MODE") == "1":
        return {"reset": project_abandonment_repository.reset()}


@router.post(
    "/project_abandonment/",
    tags=["project_postulations"],
    response_model=ProjectAbandonment,
    status_code=201,
)
async def create_project_abandonment(project_abandonment: ProjectAbandonment):
    project_update = ProjectsUpdate(state=ProjectStates.PENDING)
    ProjectsController.put(
        projects_repository,
        auxiliary_repository,
        project_abandonment.pid,
        project_update,
    )

    activity = ActivitiesRecord(action=Actions.ABANDONED, pid=project_abandonment.pid)
    ActivitiesRecordController.post(auxiliary_repository, activity)

    return ProjectAbandonmentController.post(
        project_abandonment_repository, project_abandonment
    )


@router.get(
    "/project_abandonment/",
    tags=["project_abandonment"],
    response_model=List[ProjectAbandonment],
)
async def list_project_postulations(tid: str = None, pid: str = None):
    return ProjectAbandonmentController.get(
        project_abandonment_repository, tid=tid, pid=pid
    )


@router.get(
    "/project_abandonment/{pa_id}",
    tags=["project_abandonment"],
    response_model=ProjectAbandonment,
)
async def read_project_postulations(pa_id: str):
    return ProjectAbandonmentController.get(project_abandonment_repository, pa_id=pa_id)
