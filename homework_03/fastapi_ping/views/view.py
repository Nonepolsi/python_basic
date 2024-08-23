#view.py

from fastapi import APIRouter



router = APIRouter()


@router.get(
    "/ping",
    summary="Returns pong",
    description="Returns pong to user as a response to ping"
)
def get_ping():
    return {"message": "pong"}