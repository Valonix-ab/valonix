from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
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

# Inkommande data
class ChatRequest(BaseModel):
    message: str

# Läs produktdata
with open("products.json", "r", encoding="utf-8") as f:
    products = json.load(f)

# Format produktdata till AI-vänlig HTML
def format_product_knowledge(products):
    lines = []
    for p in products:
        lines.append(f"""
<div class="product-card">
  <img src="{p['bild']}" alt="{p['namn']}" />
  <h3>{p['namn']}</h3>
  <p>{p['beskrivning']}</p>
  <p><strong>Pris:</strong> {p['pris']} SEK</p>
  <a href="{p['url']}" target="_blank">Visa produkt</a>
</div>
        """)
    return "\n".join(lines)

product_knowledge = format_product_knowledge(products)

# Extra info (öppettider, kundtjänst osv)
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

# OpenAI-klient
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

När du rekommenderar en produkt, använd följande HTML-format så att det visas snyggt i en chattwidget:

<div class="product-card">
  <img src="[BILDLÄNK]" alt="[NAMN]" />
  <h3>[NAMN]</h3>
  <p>[BESKRIVNING]</p>
  <p><strong>Pris:</strong> [PRIS] SEK</p>
  <a href="[LÄNK]" target="_blank">Visa produkt</a>
</div>

⚠️ Viktigt:
- Använd **äkta HTML** – ingen markdown, inga kodblock (inga ```).
- Undvik att escape:a HTML (använd < och > direkt).
- Ingen extra text som "Här är koden:" – returnera HTML direkt.

Svaren ska vara korta, vänliga och professionella.

Tillgängliga produkter:
{product_knowledge}

Allmän företagsinformation:
{business_info}

Om du inte vet svaret – säg det istället för att gissa.
"""
                },
                {"role": "user", "content": chat_request.message}
            ]
        )
        return {"response": response.choices[0].message.content}
    except Exception as e:
        return {"response": f"Något gick fel: {str(e)}"}
