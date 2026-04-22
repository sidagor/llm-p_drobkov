from fastapi import APIRouter, Depends, HTTPException, status

from app.api.deps import get_chat_usecase, get_current_user_id
from app.usecases.chat import ChatUseCase
from app.schemas.chat import ChatRequest, ChatResponse
from app.core.errors import ExternalServiceError


router = APIRouter(prefix="/chat", tags=["chat"])


@router.post("", response_model=ChatResponse)
async def chat(
    data: ChatRequest,
    user_id: int = Depends(get_current_user_id),
    usecase: ChatUseCase = Depends(get_chat_usecase),
):
    """
    Отправка запроса в LLM и получение ответа.
    """
    try:
        answer = await usecase.ask(
            user_id=user_id,
            prompt=data.prompt,
            system=data.system,
            max_history=data.max_history,
            temperature=data.temperature,
        )
        return {"answer": answer}

    except ExternalServiceError as e:
        raise HTTPException(
            status_code=status.HTTP_502_BAD_GATEWAY,
            detail=str(e),
        )


@router.get("/history")
async def get_history(
    user_id: int = Depends(get_current_user_id),
    usecase: ChatUseCase = Depends(get_chat_usecase),
):
    """
    Получение истории сообщений пользователя.
    """
    return await usecase.get_history(user_id)


@router.delete("/history")
async def clear_history(
    user_id: int = Depends(get_current_user_id),
    usecase: ChatUseCase = Depends(get_chat_usecase),
):
    """
    Очистка всей истории сообщений пользователя.
    """
    await usecase.clear_history(user_id)
    return {"status": "history cleared"}