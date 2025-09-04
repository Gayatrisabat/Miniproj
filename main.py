from fastapi import FastAPI
from routes import auth, game, quiz , upload

app = FastAPI(title="FinTeach Backend")

# Register routes
app.include_router(auth.router, prefix="/auth", tags=["Authentication"])
app.include_router(game.router, prefix="/game", tags=["Game"])
app.include_router(quiz.router, prefix="/quiz", tags=["Quiz"])
app.include_router(upload.router, prefix="/api", tags=["upload"])

@app.get("/")
def root():
    return {"message": "Welcome to FinTeach Backend 🚀"}
