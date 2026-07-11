from app.agents.email_agent import EmailAgent

agent = EmailAgent()

email = """

Hello,

I purchased your software yesterday.

I cannot login.

Can you help me?

"""

response = agent.analyze(email)

print("=" * 40)
print("Category :", response.category)
print("Priority :", response.priority)
print("Needs Human :", response.needs_human)

print("\nReply\n")

print(response.reply)