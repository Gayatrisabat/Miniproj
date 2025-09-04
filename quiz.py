# backend/routes/quiz.py
from fastapi import APIRouter

router = APIRouter()

# Test route
@router.get("/test")
def quiz_test():
    return {"message": "Quiz route working!"}

# Example quiz API (GET)
@router.get("/")
def get_quizzes():
    # Later, fetch quizzes from Firestore
    return {
        "quizzes": [
            {"id": 1, "question": "What is budgeting?", "options": ["A plan", "A loan", "A tax"], "answer": "A plan"},
            {"id": 2, "question": "What is EMI?", "options": ["Equated Monthly Installment", "Easy Money Income", "Extra Monthly Interest"], "answer": "Equated Monthly Installment"},
        ]
    }
