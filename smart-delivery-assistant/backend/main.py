from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import json
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from agent.logic import ask_agent

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # your frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

with open(os.path.join(os.path.dirname(__file__), "data.json")) as f:
    data = json.load(f)

@app.get("/")
def home():
    return {"message": "Smart Delivery Assistant is running!"}


@app.post("/ask")
async def ask(request: Request):
    body = await request.json()  # <--- FIX: read JSON from Axios
    q = body.get("query", "")
    answer = ask_agent(q)
    return {"query": q, "answer": answer}
