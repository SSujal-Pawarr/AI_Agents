from app.prompts.email_prompt import EMAIL_AGENT_PROMPT
from app.services.llm_service import LLMService


class EmailAgent:

    def __init__(self):

        self.llm = LLMService()

    def analyze(self, email: str):

        prompt = f"""
{EMAIL_AGENT_PROMPT}

Customer Email:

{email}
"""

        return self.llm.generate(prompt)