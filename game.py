# backend/routes/game.py
from fastapi import APIRouter

router = APIRouter()

@router.get("/game/test")
def test_game():
    return {"message": "Game route working!"}
