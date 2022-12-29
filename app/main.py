from fastapi import FastAPI
from .routers import projects, state, project_postulations


app = FastAPI()


app.include_router(projects.router)
app.include_router(state.router)
app.include_router(project_postulations.router)
