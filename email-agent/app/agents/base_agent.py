from app.services.llm_service import LLMService


class BaseAgent:

    def __init__(self):
        self.llm = LLMService()

    def generate(self, prompt: str) -> str:
        """
        Sends a prompt to the LLM.

        Every future agent will use this method.
        """

        return self.llm.generate(prompt)