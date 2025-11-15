from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.routers import chat, resume, jobmatch

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "Backend Running!"}

app.include_router(resume.router, prefix="/resume")
app.include_router(jobmatch.router, prefix="/jobmatch")
app.include_router(chat.router, prefix="/chat")
