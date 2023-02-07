import os
from typing import List
from fastapi import APIRouter

from app import config

from ..controllers.project_finished_requests_controller import (
    ProjectFinishedRequestsController,
)
from ..controllers.projects_controller import ProjectsController
from ..models.auxiliary_models.project_states import ProjectStates
from ..models.auxiliary_models.request_states import RequestStates
from ..models.project_finished_requests import ProjectFinishedRequests
from ..models.requests.project_finished_requests_update import (
    ProjectFinishedRequestsUpdate,
)
from ..models.requests.project_update import ProjectsUpdate
from ..repositories.project_finished_requests_repository import (
    ProjectFinishedRequestsRepository,
)
from .projects import projects_repository
from . import auxiliary_repository

router = APIRouter()

# Repository
project_finished_requests_repository = ProjectFinishedRequestsRepository(
    config.DATABASE_URL, config.DATABASE_NAME
)


@router.post(
    "/project_finished_requests/reset",
    tags=["project_finished_requests"],
    status_code=200,
)
async def reset():
    if os.environ.get("TEST_MODE") == "1":
        return {"reset": project_finished_requests_repository.reset()}


@router.post(
    "/project_finished_requests/",
    tags=["project_finished_requests"],
    response_model=ProjectFinishedRequests,
    status_code=201,
)
async def create_project_postulations(
    project_finished_requests: ProjectFinishedRequests,
):
    project_update = ProjectsUpdate(state=ProjectStates.FINISH_REQUEST)
    ProjectsController.put(
        projects_repository,
        auxiliary_repository,
        project_finished_requests.pid,
        project_update,
    )
    return ProjectFinishedRequestsController.post(
        project_finished_requests_repository, project_finished_requests
    )


@router.get(
    "/project_finished_requests/",
    tags=["project_finished_requests"],
    response_model=List[ProjectFinishedRequests],
)
async def list_project_postulations(tid: str = None, pid: str = None):
    return ProjectFinishedRequestsController.get(
        project_finished_requests_repository, tid=tid, pid=pid
    )


@router.get(
    "/project_finished_requests/{pfr_id}",
    tags=["project_finished_requests"],
    response_model=ProjectFinishedRequests,
)
async def read_project_postulations(pfr_id: str):
    return ProjectFinishedRequestsController.get(
        project_finished_requests_repository, pfr_id=pfr_id
    )


@router.put(
    "/project_finished_requests/{pfr_id}",
    tags=["project_postulations"],
    response_model=ProjectFinishedRequests,
)
async def update_project_postulations(
    pfr_id: str, project_finished_requests_update: ProjectFinishedRequestsUpdate
):
    request_updated = ProjectFinishedRequestsController.put(
        project_finished_requests_repository, pfr_id, project_finished_requests_update
    )
    pid = request_updated.pid
    if project_finished_requests_update.state == RequestStates.REJECTED:
        project_update = ProjectsUpdate(state=ProjectStates.WIP)
        ProjectsController.put(
            projects_repository,
            auxiliary_repository,
            pid,
            project_update,
        )
    return request_updated
