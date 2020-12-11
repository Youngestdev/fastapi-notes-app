from fastapi import FastAPI
from .routes import router as NoteRouter

app = FastAPI()

@app.get("/", tags=["Root"])
async def read_root() -> dict:
    return {
        "message": "Welcome to my notes application, use the /docs route to proceed"
    }

app.include_router(NoteRouter, prefix="/note")