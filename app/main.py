from fastapi import FastAPI
from .routers import (
    projects,
    state,
    project_postulations,
    project_abandonment,
    project_abandons_requests,
)


app = FastAPI()


app.include_router(projects.router)
app.include_router(state.router)
app.include_router(project_postulations.router)
app.include_router(project_abandonment.router)
app.include_router(project_abandons_requests.router)
