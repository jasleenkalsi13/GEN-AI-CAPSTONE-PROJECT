🚀 Gen-AI Job Application Assistant
An end-to-end system built using FastAPI (backend) and HTML/CSS/JavaScript (frontend) that helps users:
✅ Upload and analyze resumes
✅ Match job descriptions
✅ Chat with an AI assistant
✅ Use a beautiful dashboard interface
This project integrates Groq LLaMA models, resume parsing, job analysis, and real-time chat features.
🧠 Features
1️⃣ Resume Upload & AI Summary
Users can upload .pdf, .docx, or .txt resumes.
Backend extracts text and sends it to an LLM for:
Summary
Strengths
Weaknesses
Recommendation
2️⃣ Job Description Matching
Paste any job description and the AI will:
Extract required skills
Match them to candidate profile
Provide a suitability analysis
3️⃣ Chat Assistant
A chatbot powered by Groq LLaMA 8B/70B models for:
Career guidance
Job prep help
Resume improvements
General queries
4️⃣ Modern Frontend Dashboard
Beautiful, glass-UI dashboard built using:
Pure HTML
Pure CSS
Vanilla JS
📂 Project Structure
GEN-AI-CAPSTONE-PROJECT/
│── backend/
│   │── main.py
│   │── routers/
│   │   ├── resume.py
│   │   ├── chat.py
│   │   └── jobmatch.py
│── frontend/
│   ├── index.html
│   ├── style.css
│   └── script.js
│── README.md
⚙️ Technologies Used
Backend
FastAPI
Python 3.10+
Groq API (LLAMA3)
PyPDF2
docx2txt
CORS Middleware
Frontend
HTML
CSS (Gradient UI + Glassmorphism)
JavaScript (Fetch API)
🛠 Backend Setup Instructions
1️⃣ Clone the repository
git clone <your-repo-url>
cd GEN-AI-CAPSTONE-PROJECT
2️⃣ Create a virtual environment
python3 -m venv venv
source venv/bin/activate     # macOS / Linux
venv\Scripts\activate        # Windows
3️⃣ Install dependencies
pip install -r requirements.txt
4️⃣ Add your Groq API Key
Create .env inside backend folder:
GROQ_API_KEY=your_key_here
5️⃣ Run FastAPI
uvicorn backend.main:app --reload
Backend runs at:
👉 http://127.0.0.1:8000
💻 Frontend Setup Instructions
Just open the file:
frontend/index.html
Or run a simple server:
cd frontend
python3 -m http.server
Frontend runs at:
👉 http://127.0.0.1:8000 (if served)
OR
👉 file path (if opened directly)
🔌 API Endpoints
1. Resume Upload
POST /resume/upload
Request: multipart/form-data
Body: resume file
2. Job Match
POST /jobmatch/match
Request Body:
{
  "job_description": "text here"
}
3. Chat Query
POST /chat/query
Request Body:
{
  "question": "Your question"
}
🧪 Testing the API
Use Postman or cURL.
Example:
curl -X POST "http://127.0.0.1:8000/chat/query" \
  -H "Content-Type: application/json" \
  -d '{"question":"How to improve my resume?"}'
🎨 Screenshots (Add your own)
Add UI screenshots here:
/frontend/screenshots/resume_page.png
/frontend/screenshots/chat_page.png
🏁 Final Notes
✔ Fully functional AI Job Assistant
✔ Beautiful dashboard UI
✔ Groq-powered resume + job understanding
✔ Clean backend architecture
✔ Ideal for MCA, Projects, Portfolio, Internship Submission
🙌 Contributors
Jasleen-LEADER
Anushree-LEAD
Vaishnavi-LEAD
