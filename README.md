🚀 GEN-AI Capstone Project
A complete end-to-end Gen-AI Application built using Python, FastAPI/Flask (Backend) and React/Next.js (Frontend).
This project integrates LLMs, RAG (Retrieval Augmented Generation), vector embeddings, and Groq API to deliver intelligent responses based on uploaded content/documents.
🔥 Project Features
🧠 AI Features
LLM-powered chatbot using Groq API / Llama / Mixtral
RAG pipeline using vector embedding + similarity search
Supports document-based Q&A
Context-aware, accurate responses
Fast inference with Groq’s low-latency API
📂 Backend (Python)
FastAPI/Flask server
Embedding generation
Vector database integration (FAISS / Chroma)
API endpoints:
/upload – upload documents
/process – embed + index
/ask – query the model
Environment variables stored in .env
Secure secret handling (Git ignored)
🖥 Frontend
Modern UI (React / HTML / CSS / Bootstrap / Tailwind)
Chat interface with user & bot messages
File upload interface
Loading animation for AI responses
Error handling + validations
🧑‍💻 Tech Stack
Component	Technology
Frontend	ReactJS / HTML / CSS / JavaScript
Backend	Python, FastAPI/Flask
AI API	Groq API (Llama / Mixtral models)
Vector DB	FAISS / Chroma
Embeddings	SentenceTransformers / HuggingFace
Version Control	Git & GitHub
📁 Project Structure
GEN-AI-CAPSTONE-PROJECT/
│
├── backend/
│   ├── app.py (main backend file)
│   ├── rag_engine.py
│   ├── vector_db/
│   ├── uploads/
│   ├── .env (ignored)
│   └── requirements.txt
│
├── frontend/
│   ├── src/
│   ├── public/
│   └── package.json
│
├── README.md
└── .gitignore
⚙️ Setup Instructions
1️⃣ Clone the Repo
git clone https://github.com/jasleenkalsi13/GEN-AI-CAPSTONE-PROJECT.git
cd GEN-AI-CAPSTONE-PROJECT
🖥 Backend Setup
2️⃣ Create Virtual Environment
cd backend
python3 -m venv venv
source venv/bin/activate   # Mac/Linux
3️⃣ Install Requirements
pip install -r requirements.txt
4️⃣ Create .env File
Create a .env inside backend/:
GROQ_API_KEY=your_api_key_here
MODEL_NAME=llama-3.1
5️⃣ Run Backend
python app.py
Backend will start at:
http://localhost:5000
🌐 Frontend Setup
cd frontend
npm install
npm start
Frontend runs at:
http://localhost:3000
🧪 How to Use
Start backend
Start frontend
Upload your documents (PDF/TXT)
Ask questions in the chatbot
AI will respond using your uploaded content (RAG)
🛡️ Security Notes
.env file is ignored using .gitignore
Do NOT upload API keys to GitHub
Regenerate your Groq API key if previously exposed
🤝 Contributing
Pull requests are welcome!
Feel free to open issues or suggest enhancements.
⭐ Show Your Support
If this project helped you, please star the repository ⭐ on GitHub!
