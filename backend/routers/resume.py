from fastapi import APIRouter, UploadFile, File
from groq import Groq
import os
import docx2txt
import tempfile
from PyPDF2 import PdfReader
from dotenv import load_dotenv

load_dotenv()
router = APIRouter()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def extract_text(file: UploadFile):
    # create temp file
    with tempfile.NamedTemporaryFile(delete=False) as tmp:
        tmp.write(file.file.read())
        tmp_path = tmp.name

    if file.filename.endswith(".pdf"):
        reader = PdfReader(tmp_path)
        text = ""
        for page in reader.pages:
            text += page.extract_text() or ""
        return text

    elif file.filename.endswith(".docx"):
        return docx2txt.process(tmp_path)

    elif file.filename.endswith(".txt"):
        with open(tmp_path, "r") as f:
            return f.read()

    return "Unsupported file format"


@router.post("/upload")
async def upload_resume(file: UploadFile = File(...)):

    text = extract_text(file)

    prompt = f"""
    Summarize this resume in 4-5 lines.
    Resume Text:
    {text}
    """

    response = client.chat.completions.create(
        model="llama3-70b-8192",
        messages=[{"role": "user", "content": prompt}]
    )

    summary = response.choices[0].message.content

    return {"summary": summary}
