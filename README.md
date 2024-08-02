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

