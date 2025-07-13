from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

# Tillåt frontend att prata med API:et
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Byt till din domän i produktion
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Dataformat för inkommande meddelanden
class ChatRequest(BaseModel):
    message: str

# OpenAI-klient
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

@app.post("/chat")
async def chat(chat_request: ChatRequest):
    try:
        response = client.chat.completions.create(
            model="gpt-4o",  # GPT-4o används här
            messages=[
                {"role": "system", "content": "Du är en hjälpsam AI-assistent."},
                {"role": "user", "content": chat_request.message}
            ]
        )
        return {"response": response.choices[0].message.content}
    except Exception as e:
        return {"response": f"Något gick fel: {str(e)}"}
