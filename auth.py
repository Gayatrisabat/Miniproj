from fastapi import APIRouter
from pydantic import BaseModel
from database.firebase import db

router = APIRouter()

class User(BaseModel):
    email: str
    password: str
    name: str

@router.post("/register")
def register(user: User):
    user_ref = db.collection("users").document(user.email)
    if user_ref.get().exists:
        return {"error": "User already exists"}
    user_ref.set(user.dict())
    return {"message": "User registered successfully"}

@router.post("/login")
def login(user: User):
    user_ref = db.collection("users").document(user.email).get()
    if not user_ref.exists:
        return {"error": "User not found"}
    data = user_ref.to_dict()
    if data["password"] != user.password:
        return {"error": "Invalid credentials"}
    return {"message": "Login successful"}
