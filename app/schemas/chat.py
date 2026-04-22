from pydantic import BaseModel, Field
from typing import Optional


class ChatRequest(BaseModel):
    """
    Схема запроса к LLM.
    """

    prompt: str = Field(
        min_length=1,
        description="User input text",
    )

    system: Optional[str] = Field(
        default=None,
        description="Optional system instruction",
    )

    max_history: int = Field(
        default=10,
        ge=0,
        le=100,
        description="Number of previous messages to include",
    )

    temperature: float = Field(
        default=0.7,
        ge=0.0,
        le=1.0,
        description="Model creativity level",
    )


class ChatResponse(BaseModel):
    """
    Схема ответа от LLM.
    """
    answer: str