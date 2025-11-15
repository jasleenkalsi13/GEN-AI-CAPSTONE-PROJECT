from fastapi import APIRouter
from pydantic import BaseModel
from groq import Groq
import os

router = APIRouter()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

class ChatRequest(BaseModel):
    question: str

@router.post("/query")
async def chat(req: ChatRequest):
    response = client.chat.completions.create(
        model="llama3-8b-8192",
        messages=[{"role": "user", "content": req.question}]
    )
    answer = response.choices[0].message.content
    return {"answer": answer}
