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

app = FastAPI()

# CORS: så widgeten kan bäddas in på andra sidor
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Serve frontend-filer
@app.get("/")
def serve_index():
    return FileResponse("index.html")

@app.get("/widget.html")
def serve_widget_html():
    return FileResponse("widget.html")

@app.get("/widget.js")
def serve_widget_js():
    return FileResponse("widget.js", media_type="application/javascript")

# Mount static files om du har bilder, CSS, fonts osv i roten
app.mount("/static", StaticFiles(directory="."), name="static")

# Datamodell för inkommande meddelanden
class ChatRequest(BaseModel):
    message: str

# OpenAI-klienten (GPT-4o)
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

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
