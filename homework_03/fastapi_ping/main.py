#main.py

from fastapi import FastAPI
from views import router as views_router



app = FastAPI(
    title="App for pinging",
    description="App which returns pong for ping request",
    version="1.0.0"
)


app.include_router(views_router)