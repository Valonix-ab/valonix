from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from openai import OpenAI
from dotenv import load_dotenv
import os
import json

# Ladda miljövariabler (som OPENAI_API_KEY)
load_dotenv()

app = FastAPI()

# CORS: så widgeten kan bäddas in externt
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Frontend routes
@app.get("/")
def serve_index():
    return FileResponse("index.html")

@app.get("/widget.html")
def serve_widget_html():
    return FileResponse("widget.html")

@app.get("/widget.js")
def serve_widget_js():
    return FileResponse("widget.js", media_type="application/javascript")

# Statisk mapp
app.mount("/static", StaticFiles(directory="."), name="static")

# Inkommande data
class ChatRequest(BaseModel):
    message: str

# 🟩 Läs in produktdata från products.json
with open("products.json", "r", encoding="utf-8") as f:
    products = json.load(f)

# Format produktdata till en promptvänlig text
def format_product_knowledge(products):
    lines = []
    for p in products:
        lines.append(
            f"""- {p['namn']} ({p['kategori']}): {p['beskrivning']} 
  Pris: {p['pris']} SEK
  Länk: {p['url']}
  Bild: {p.get('bild', 'Ingen bild')}"""
        )
    return "\n".join(lines)

product_knowledge = format_product_knowledge(products)

# 🟦 Extra info som öppettider, kundtjänst mm
business_info = """
Öppettider (generella):
- Vardagar: 10:00–19:00
- Lördagar: 10:00–17:00
- Söndagar: 11:00–16:00

Kundtjänst:
- Telefon: 0770–457 457
- E-post: kundservice@jysk.se
- Chatt: Öppen vardagar 9–17

Butiksinformation:
- Du kan hitta närmaste butik på: https://jysk.se/stores
- Vi erbjuder både hemleverans och avhämtning i butik.
"""

# OpenAI klient
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

@app.post("/chat")
async def chat(chat_request: ChatRequest):
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "system",
                    "content": f"""Du är en AI-assistent för JYSK Sverige.
Du ska ge professionella svar på frågor om:
- Produkter (se lista nedan)
- Öppettider
- Butiksinformation
- Leveransalternativ
- Kundtjänst

Produktinformation:
{product_knowledge}

Allmän företagsinformation:
{business_info}

Om du inte vet något, säg ärligt att du inte har tillgång till den informationen.
"""
                },
                {"role": "user", "content": chat_request.message}
            ]
        )
        return {"response": response.choices[0].message.content}
    except Exception as e:
        return {"response": f"Något gick fel: {str(e)}"}
