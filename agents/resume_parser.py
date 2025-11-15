# agents/resume_parser.py

import asyncio
import pdfplumber
import re

class ResumeParserAgent:
    """
    Extracts text from resume PDF and returns a clean structured dict.
    No external API key required.
    """

    def __init__(self, llm_client=None):
        self.llm_client = llm_client  # optional (Gemini if needed later)

    async def parse(self, resume_path):
        """
        Async method to allow parallel execution with JD parsing.
        """
        text = await self._extract_text(resume_path)
        structured = self._structure(text)
        return structured

    async def _extract_text(self, path):
        """
        Extracts raw text from a PDF using pdfplumber.
        """
        def read_pdf():
            with pdfplumber.open(path) as pdf:
                pages = [page.extract_text() or "" for page in pdf.pages]
                return "\n".join(pages)

        # Run extraction in thread (pdfplumber is blocking)
        loop = asyncio.get_event_loop()
        return await loop.run_in_executor(None, read_pdf)

    def _structure(self, text):
        """
        Very basic structuring (you can improve later):
        Extract name, email, phone, skills.
        """
        email = re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", text)
        phone = re.findall(r"\+?\d[\d -]{8,}\d", text)
        skills = re.findall(r"Skills[\s:]*([\s\S]+?)(Experience|Projects|$)", text, re.I)

        return {
            "raw_text": text[:5000],  # limit to avoid oversized output
            "email": email[0] if email else None,
            "phone": phone[0] if phone else None,
            "skills": skills[0][0].strip() if skills else None
        }
