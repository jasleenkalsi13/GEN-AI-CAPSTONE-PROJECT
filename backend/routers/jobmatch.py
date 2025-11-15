from fastapi import APIRouter
from pydantic import BaseModel
from groq import Groq
import os

router = APIRouter()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

class JobRequest(BaseModel):
    job_description: str

@router.post("/match")
async def match_job(req: JobRequest):
    prompt = f"""
    Analyze this job description and return a short summary
    and required skills:

    {req.job_description}
    """

    response = client.chat.completions.create(
        model="llama3-70b-8192",
        messages=[{"role": "user", "content": prompt}]
    )

    result = response.choices[0].message.content
    return {"match_result": result}
