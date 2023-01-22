import os
from typing import List
from fastapi import APIRouter

from app import config
from . import auxiliary_repository
from ..controllers.project_abandons_requests_controller import (
    ProjectAbandonsRequestsController,
)
from ..controllers.projects_controller import ProjectsController
from ..models.auxiliary_models.project_states import ProjectStates
from ..models.project_abandons_requests import ProjectAbandonsRequests
from ..models.requests.project_abandons_requests_update import (
    ProjectAbandonsRequestsUpdate,
)
from ..models.requests.project_update import ProjectsUpdate
from ..repositories.project_abandons_requests_repository import (
    ProjectAbandonsRequestsRepository,
)
from .projects import projects_repository


router = APIRouter()

# Repository
project_abandons_requests_repository = ProjectAbandonsRequestsRepository(
    config.DATABASE_URL, config.DATABASE_NAME
)


@router.post(
    "/project_abandons_requests/reset",
    tags=["project_abandons_requests"],
    status_code=200,
)
async def reset():
    if os.environ.get("TEST_MODE") == "1":
        return {"reset": project_abandons_requests_repository.reset()}


@router.post(
    "/project_abandons_requests/",
    tags=["project_abandons_requests"],
    response_model=ProjectAbandonsRequests,
    status_code=201,
)
async def create_project_postulations(
    project_abandons_requests: ProjectAbandonsRequests,
):
    project_update = ProjectsUpdate(state=ProjectStates.ABANDONS_REQUEST)
    ProjectsController.put(
        projects_repository,
        auxiliary_repository,
        project_abandons_requests.pid,
        project_update,
    )
    return ProjectAbandonsRequestsController.post(
        project_abandons_requests_repository, project_abandons_requests
    )


@router.get(
    "/project_abandons_requests/",
    tags=["project_abandons_requests"],
    response_model=List[ProjectAbandonsRequests],
)
async def list_project_postulations(tid: str = None, pid: str = None):
    return ProjectAbandonsRequestsController.get(
        project_abandons_requests_repository, tid=tid, pid=pid
    )


@router.get(
    "/project_abandons_requests/{par_id}",
    tags=["project_abandons_requests"],
    response_model=ProjectAbandonsRequests,
)
async def read_project_postulations(par_id: str):
    return ProjectAbandonsRequestsController.get(
        project_abandons_requests_repository, par_id=par_id
    )


@router.put(
    "/project_abandons_requests/{par_id}",
    tags=["project_postulations"],
    response_model=ProjectAbandonsRequests,
)
async def update_project_postulations(
    par_id: str, project_abandons_requests_update: ProjectAbandonsRequestsUpdate
):
    return ProjectAbandonsRequestsController.put(
        project_abandons_requests_repository, par_id, project_abandons_requests_update
    )
