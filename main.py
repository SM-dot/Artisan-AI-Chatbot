from fastapi import FastAPI, Request
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
import openai


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

#openai.api_key = "enter your key here"

class ChatRequest(BaseModel):
    message: str
    chat_id: str

memory = {}

@app.post("/chat")
async def chat(chat_request: ChatRequest):
    chat_id = chat_request.chat_id
    message = chat_request.message

    if chat_id not in memory:
        memory[chat_id] = []

    memory[chat_id].append({"role": "user", "content": message})

    d = ""
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=memory[chat_id] + [{"role": "system", "content": """
        You are Ava a virtual employee of Artisan AI. \
        Introduce yourself as Ava - an assisstant to help the user find the perfect solution for them using Artisan AIs features. Ask their name and what they need help with. \
        You answer questions in a friendly precise manner on behalf of Artisan AI.\
        In cases when you do not know enough information. Honestly tell the user that you will check and get back to them.\
        Information about Artisan AI: 
        Artisan AI's Sales AI platform automates and optimizes outbound sales tasks. It offers features like a comprehensive B2B data database, email warmup, AI-driven sales playbooks,\
        and automated outbound workflow management. The platform's AI agent, Ava, handles lead identification, prospect research, and email drafting, freeing sales teams to focus on high-leverage activities. \
        Additionally, the platform provides detailed analytics for tracking and optimizing sales strategies.\
        """}]
    )

    answer = response.choices[0].message['content']
    memory[chat_id].append({"role": "assistant", "content": answer})

    return {"answer": answer}

app.mount("/", StaticFiles(directory=".", html=True), name="static")
