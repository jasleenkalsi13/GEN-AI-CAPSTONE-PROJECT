from fastapi import APIRouter
from pydantic import BaseModel
from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()

router = APIRouter()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

class ChatRequest(BaseModel):
    message: str

@router.post("/")
async def chat_agent(req: ChatRequest):
    response = client.chat.completions.create(
        model="llama3-8b-8192",
        messages=[
            {"role": "system", "content": "You are an AI assistant helping with general questions."},
            {"role": "user", "content": req.message}
        ]
    )

    reply = response.choices[0].message.content
    return {"reply": reply}
