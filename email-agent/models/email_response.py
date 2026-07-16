from pydantic import BaseModel
from typing import Literal

class EmailResponse(BaseModel):
    category: Literal[
        "Support",
        "Sales",
        "Billing",
        "Refund",
        "Technical Issue",
        "Complaint",
        "Feature Request",
        "General Inquiry",
        "Spam",
    ]

    priority: Literal[
        "Low",
        "Medium",
        "High",
    ]

    needs_human: bool

    reply: str