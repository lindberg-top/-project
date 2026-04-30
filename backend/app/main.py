from fastapi import FastAPI
from backend.app.api.users import router as users_router
from backend.app.api import subscriptions

app = FastAPI()

app.include_router(users_router)
app.include_router(subscriptions.router)