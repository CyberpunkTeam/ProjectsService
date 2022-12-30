import os
from typing import List

from fastapi import APIRouter

from app import config
from app.controllers.project_postulations_controller import (
    ProjectPostulationsController,
)
from app.models.project_postulations import ProjectPostulations
from app.repositories.project_postulations_repository import (
    ProjectPostulationsRepository,
)
from .projects import projects_repository
from ..models.requests.project_postulations_update import ProjectPostulationsUpdate
from ..models.states import States

router = APIRouter()

# Repository
project_postulations_repository = ProjectPostulationsRepository(
    config.DATABASE_URL, config.DATABASE_NAME
)


@router.post("/projects/postulations/reset", tags=["team_invitations"], status_code=200)
async def reset():
    if os.environ.get("TEST_MODE") == "1":
        return {"reset": project_postulations_repository.reset()}


@router.post(
    "/projects/postulations/",
    tags=["project_postulations"],
    response_model=ProjectPostulations,
    status_code=201,
)
async def create_project_postulations(project_postulation: ProjectPostulations):
    project = projects_repository.get(pid=project_postulation.pid)[0]
    project_postulation.project_owner_uid = project.creator_uid
    return ProjectPostulationsController.post(
        project_postulations_repository, project_postulation
    )


@router.get(
    "/projects/postulations/",
    tags=["project_postulations"],
    response_model=List[ProjectPostulations],
)
async def list_project_postulations(
    tid: str = None, pid: str = None, state: States = None
):
    return ProjectPostulationsController.get(
        project_postulations_repository, tid=tid, pid=pid, state=state
    )


@router.get(
    "/projects/postulations/{ppid}",
    tags=["project_postulations"],
    response_model=ProjectPostulations,
)
async def read_project_postulations(ppid: str):
    return ProjectPostulationsController.get(project_postulations_repository, ppid=ppid)


@router.put(
    "/projects/postulations/{pid}",
    tags=["project_postulations"],
    response_model=ProjectPostulations,
)
async def update_project_postulations(
    pid: str, project_update: ProjectPostulationsUpdate
):
    return ProjectPostulationsController.put(
        project_postulations_repository, pid, project_update
    )
