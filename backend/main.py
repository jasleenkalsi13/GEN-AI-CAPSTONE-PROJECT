from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="GEN AI Capstone Project API",
    description="API for Job Application Assistant, Resume Evaluation & Job Matching",
    version="1.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "GEN-AI Capstone API is running successfully!"}

# Routers
from backend.routers import chat, resume, jobmatch

app.include_router(chat.router, prefix="/chat", tags=["Chat Assistant"])
app.include_router(resume.router, prefix="/resume", tags=["Resume Evaluation"])
app.include_router(jobmatch.router, prefix="/jobmatch", tags=["Job Matching"])
