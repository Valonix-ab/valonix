from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from openai import OpenAI
from dotenv import load_dotenv
import os

# Load environment variables (like OPENAI_API_KEY)
load_dotenv()

# Create FastAPI app
app = FastAPI()

# Enable CORS for widget embedding
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Serve index.html at root
@app.get("/")
def serve_index():
    return FileResponse("index.html")

# ✅ Serve widget.js directly at /widget.js
@app.get("/widget.js")
def serve_widget():
    return FileResponse("widget.js", media_type="application/javascript")

# ✅ Optional: mount all other assets in current directory (CSS, images, etc.)
app.mount("/static", StaticFiles(directory="."), name="static")

# Chat input format
class ChatRequest(BaseModel):
    message: str

# OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# POST endpoint for chat messages
@app.post("/chat")
async def chat(chat_request: ChatRequest):
    try:
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "Du är en hjälpsam AI-assistent."},
                {"role": "user", "content": chat_request.message}
            ]
        )
        return {"response": response.choices[0].message.content}
    except Exception as e:
        return {"response": f"Något gick fel: {str(e)}"}
