# agents/jd_analyzer.py

import re
import asyncio

class JDAnalyzerAgent:
    """
    Reads job description text and extracts:
    - required skills
    - responsibilities
    - experience level
    """

    def __init__(self, llm_client=None):
        self.llm_client = llm_client  # optional (Gemini can be added later)

    async def analyze(self, job_text):
        """
        Async method to allow parallel execution.
        """
        await asyncio.sleep(0)  # yields control to event loop
        return self._structure(job_text)

    def _structure(self, txt):
        """
        Basic pattern extraction. You can improve later.
        """
        skills = re.findall(r"skills?:([\s\S]+?)(responsibilities|requirements|$)", txt, re.I)
        responsibilities = re.findall(r"responsibilities?:([\s\S]+?)(requirements|skills|$)", txt, re.I)
        experience = re.findall(r"(\d+\+?\s*years)", txt, re.I)

        return {
            "raw_text": txt[:3000],
            "skills_required": skills[0][0].strip() if skills else None,
            "responsibilities": responsibilities[0][0].strip() if responsibilities else None,
            "experience_required": experience[0] if experience else None
        }
