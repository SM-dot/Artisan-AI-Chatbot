# Artisan AI Chatbot

This is a FastAPI-based chatbot application for Artisan AI, utilizing OpenAI's GPT-3.5 model. The chatbot is designed to provide assistance and answer questions regarding Artisan AI's features and services.

## Features

- FastAPI for creating RESTful APIs.
- Pydantic for data validation.
- OpenAI GPT-3.5 for generating responses.
- Memory to maintain conversation context.
- CORS middleware for handling cross-origin requests.
- Static file serving.

## Installation

### Prerequisites

- Python 3.7+
- An OpenAI API key

### Setup

1. **Clone the repository:**

    ```sh
    git clone https://github.com/your-username/artisan-ai-chatbot.git
    cd artisan-ai-chatbot
    ```

2. **Create a virtual environment:**

    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install dependencies:**

    ```sh
    pip install -r requirements.txt
    ```

4. **Set your OpenAI API key:**

    Replace `your-openai-api-key` in `main.py` with your actual OpenAI API key.

    ```python
    openai.api_key = "your-openai-api-key"
    ```

5. **Run the application:**

    ```sh
    uvicorn main:app --reload
    ```

6. **Access the application:**

    Open your web browser and go to `http://127.0.0.1:8000`.

## Usage

- **Chat Endpoint:** 
  - URL: `/chat`
  - Method: `POST`
  - Request Body: 
    ```json
    {
      "message": "your message here",
      "chat_id": "unique_chat_id"
    }
    ```

- **Static Files:**
  - The application serves static files from the root directory. You can place your static files (like HTML, CSS, JS) in the project root.

## Code Explanation

### main.py

This is the main entry point of the application. It sets up the FastAPI app, includes middleware, and defines the chat endpoint.

```python
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

openai.api_key = "your-openai-api-key"

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
        You are Ava, a virtual employee of Artisan AI. Introduce yourself as Ava - an assistant to help the user find the perfect solution for them using Artisan AI's features. Ask their name and what they need help with. You answer questions in a friendly, precise manner on behalf of Artisan AI. In cases when you do not know enough information, honestly tell the user that you will check and get back to them.
        Information about Artisan AI: 
        Artisan AI's Sales AI platform automates and optimizes outbound sales tasks. It offers features like a comprehensive B2B data database, email warmup, AI-driven sales playbooks, and automated outbound workflow management. The platform's AI agent, Ava, handles lead identification, prospect research, and email drafting, freeing sales teams to focus on high-leverage activities. Additionally, the platform provides detailed analytics for tracking and optimizing sales strategies.
        """}]
    )

    answer = response.choices[0].message['content']
    memory[chat_id].append({"role": "assistant", "content": answer})

    return {"answer": answer}

app.mount("/", StaticFiles(directory=".", html=True), name="static")
```
## Pydantic Model
ChatRequest is a Pydantic model used for validating the incoming request data. It ensures that the request contains a message and a chat_id.

## Memory
A dictionary memory is used to store the conversation history for each chat_id. This allows the chatbot to maintain context and provide more relevant responses.

## OpenAI GPT-3.5 Integration
The chatbot uses OpenAI's GPT-3.5 model to generate responses based on the conversation history stored in memory.

## CORS Middleware
The CORSMiddleware is configured to allow cross-origin requests from any origin. This is useful for enabling the frontend to interact with the API without CORS issues.

## Static File Serving
The application serves static files from the root directory, allowing you to serve an HTML frontend alongside the FastAPI backend.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.
