from fastapi import FastAPI
from .routers import (
    projects,
    state,
    project_postulations,
    project_abandonment,
    project_abandons_requests,
    project_finished_requests,
    projects_reviews,
)


app = FastAPI()


app.include_router(projects.router)
app.include_router(state.router)
app.include_router(project_postulations.router)
app.include_router(project_abandonment.router)
app.include_router(project_abandons_requests.router)
app.include_router(project_finished_requests.router)
app.include_router(projects_reviews.router)
