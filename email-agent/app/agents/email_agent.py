import json

from app.agents.base_agent import BaseAgent
from app.models.email_response import EmailResponse
from app.prompts.email_prompt import EMAIL_AGENT_PROMPT


class EmailAgent(BaseAgent):

    def analyze(self, email: str) -> EmailResponse:

        prompt = f"""
{EMAIL_AGENT_PROMPT}

Customer Email:

{email}
"""

        raw_response = self.generate(prompt)

        print("\n===== RAW LLM RESPONSE =====\n")
        print(raw_response)
        print("\n============================\n")

        data = json.loads(raw_response)

        return EmailResponse.model_validate(data)