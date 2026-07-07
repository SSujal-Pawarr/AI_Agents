from llm import ask_llm
from prompts import EMAIL_AGENT_PROMPT

email = """
Hello,

I purchased your software yesterday.

I cannot login.

Can you help me?
"""


prompt = f"""
{EMAIL_AGENT_PROMPT}

Customer Email:

{email}
"""

reply = ask_llm(prompt)

print(reply)
