from fastapi import FastAPI
from .routers import projects, state


app = FastAPI()


app.include_router(projects.router)
app.include_router(state.router)
