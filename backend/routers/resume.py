from fastapi import APIRouter
from pydantic import BaseModel
from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()

router = APIRouter()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

class ResumeRequest(BaseModel):
    resume_text: str

@router.post("/evaluate")
async def evaluate_resume(req: ResumeRequest):

    prompt = f"""
    You are a professional HR resume evaluator.
    Analyze the following resume and return ONLY valid JSON.

    Resume:
    {req.resume_text}

    Return JSON with:
    - score (0-100)
    - strengths (list)
    - weaknesses (list)
    - recommendations (list)
    - summary (short description)
    """

    response = client.chat.completions.create(
        model="llama3-70b-8192",
        messages=[{"role": "user", "content": prompt}]
    )

    result = response.choices[0].message.content
    return {"evaluation": result}
