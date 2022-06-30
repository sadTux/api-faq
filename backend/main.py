from fastapi import FastAPI
from .routes.auth import apiRouter as routerAuth
from .routes.user import apiRouter as routerUser
from .routes.question import apiRouter as routerQuestion
from starlette.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(routerAuth, prefix="/auth", tags=["login"])
app.include_router(routerUser, prefix="/user", tags=["user"])
app.include_router(routerQuestion, prefix="/question", tags=["question"])
