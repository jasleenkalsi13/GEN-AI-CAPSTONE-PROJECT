from fastapi import APIRouter
from pydantic import BaseModel
from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()

router = APIRouter()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

class JobMatchRequest(BaseModel):
    resume_text: str
    job_description: str

@router.post("/match")
async def match_job(req: JobMatchRequest):

    prompt = f"""
    You are an ATS Job Matching Agent.
    Compare the resume with the job description and return ONLY JSON.

    Resume:
    {req.resume_text}

    Job Description:
    {req.job_description}

    Return JSON:
    - match_score (0-100)
    - missing_skills (list)
    - matching_skills (list)
    - how_to_improve (list)
    """

    response = client.chat.completions.create(
        model="llama3-70b-8192",
        messages=[{"role": "user", "content": prompt}]
    )

    result = response.choices[0].message.content
    return {"job_match": result}
