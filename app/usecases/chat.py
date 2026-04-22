from app.repositories.chat_messages import ChatMessageRepository
from app.services.openrouter_client import OpenRouterClient
from app.core.errors import ExternalServiceError


class ChatUseCase:
    """
    Бизнес-логика общения с LLM.
    """
     
    def __init__(
        self,
        chat_repo: ChatMessageRepository,
        openrouter_client: OpenRouterClient,
    ):
        self._chat_repo = chat_repo
        self._client = openrouter_client
    
    async def ask(
        self,
        user_id: int,
        prompt: str,
        system: str | None = None,
        max_history: int = 10,
        temperature: float = 0.7,
    ) -> str:
        """
        Отправляет запрос в LLM с учётом истории.
        """

        messages = []

        if system:
            messages.append({
                "role": "system",
                "content": system,
            })

        history = await self._chat_repo.get_last_messages(
            user_id=user_id,
            limit=max_history,
        )

        for msg in history:
            messages.append({
                "role": msg.role,
                "content": msg.content,
            })

        messages.append({
            "role": "user",
            "content": prompt,
        })
        
        await self._chat_repo.add_message(
            user_id=user_id,
            role="user",
            content=prompt,
        )

        try:
            answer = await self._client.chat(
                messages=messages,
                temperature=temperature,
            )
        except Exception as e:
            raise ExternalServiceError(str(e))
        
        await self._chat_repo.add_message(
            user_id=user_id,
            role="assistant",
            content=answer,
        )

        return answer
    
    async def get_history(
        self,
        user_id: int,
        limit: int = 50,
    ):
        """
        Получает историю чата. 
        """
        history = await self._chat_repo.get_last_messages(
            user_id=user_id,
            limit=limit,
        )
        
        return [
            {
                "role": msg.role,
                "content": msg.content,
                "created_at": msg.created_at,
            }
            for msg in history
        ]
    
    async def clear_history(
        self,
        user_id: int,
    ) -> None:
        """
        Очищает историю чата.
        """
        await self._chat_repo.delete_all_by_user(user_id)