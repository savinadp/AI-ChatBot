import os
from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
import ollama

# Choose a model that runs on your machine:
MODEL = "llama3.1:8b-instruct-q4_0"  

app = FastAPI(title="Ollama Web Chat")

BASE_DIR = os.path.dirname(__file__)
STATIC_DIR = os.path.join(BASE_DIR, "static")

app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")


@app.get("/")
def home():
    return FileResponse(os.path.join(STATIC_DIR, "index.html"))


class ChatRequest(BaseModel):
    messages: list[dict]  # [{"role":"user","content":"hi"}, ...]
    model: str | None = None


@app.post("/chat")
def chat(req: ChatRequest):
    model = req.model or MODEL
    resp = ollama.chat(model=model, messages=req.messages)
    return {"message": resp["message"], "model": model}