from gpt4all import GPT4All
import requests
import os

BACKEND_URL = "http://localhost:8000"

MODEL_DIR = r"E:\AI\smart-delivery-assistant\agent"
MODEL_FILENAME = "orca-mini-3b-gguf2-q4_0.gguf"

gptj = GPT4All(
    MODEL_FILENAME,
    model_path=MODEL_DIR,
    allow_download=False
)

def ask_agent(query: str) -> str:
    system_prompt = (
        "You are a logistics assistant.\n"
        "If the user asks about a package, call /track-order.\n"
        "If the user asks about driver or route, call /route.\n"
        "Respond concisely in natural language.\n"
    )

    prompt = f"{system_prompt}\nUser: {query}\nAssistant:"
    response = gptj.generate(prompt, max_tokens=100)

    try:
        if "order" in query.lower():
            order_id = query.split()[-1]
            res = requests.get(f"{BACKEND_URL}/track-order/{order_id}")
            if res.status_code != 200:
                return f"Order {order_id} not found."
            data = res.json()
            if data.get("status") == "not found":
                return f"Order {order_id} not found."
            return f"Your package is {data['status']} at {data['location']}, ETA: {data['eta']}."

        elif "driver" in query.lower() or "route" in query.lower():
            driver_id = "driver101"
            res = requests.get(f"{BACKEND_URL}/route/{driver_id}")
            if res.status_code != 200:
                return "Driver not found."
            data = res.json()
            if data.get("status") == "driver not found":
                return "Driver not found."
            return f"Next stop: {data['next_stop']}, ETA {data['eta']}, via {data['route']}."

    except requests.exceptions.RequestException as e:
        return f"Backend connection error: {e}"

    return response
