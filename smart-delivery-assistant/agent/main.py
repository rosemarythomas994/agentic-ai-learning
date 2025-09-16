from fastapi import FastAPI
from agent.logic import ask_agent  # make sure this import works

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Smart Delivery Assistant is running!"}

@app.get("/ask")
def ask(query: str):
    answer = ask_agent(query)
    return {"query": query, "answer": answer}
