from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.session import AsyncSessionLocal
from app.repositories.users import UserRepository
from app.repositories.chat_messages import ChatMessageRepository
from app.usecases.auth import AuthUseCase
from app.usecases.chat import ChatUseCase
from app.services.openrouter_client import OpenRouterClient
from app.core.security import decode_token


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")



async def get_db() -> AsyncSession:
    """Dependency для получения асинхронной сессии базы данных."""
    async with AsyncSessionLocal() as session:
        yield session



def get_user_repo(
    session: AsyncSession = Depends(get_db),
) -> UserRepository:
    """Dependency для получения репозитория пользователей."""
    return UserRepository(session)


def get_chat_repo(
    session: AsyncSession = Depends(get_db),
) -> ChatMessageRepository:
    """Dependency для получения репозитория чата."""
    return ChatMessageRepository(session)


def get_openrouter_client() -> OpenRouterClient:
    """Dependency для получения клиента OpenRouter."""
    return OpenRouterClient()


def get_auth_usecase(
    user_repo: UserRepository = Depends(get_user_repo),
) -> AuthUseCase:
    """Dependency для бизнес-логики аутентификации."""
    return AuthUseCase(user_repo)


def get_chat_usecase(
    chat_repo: ChatMessageRepository = Depends(get_chat_repo),
    client: OpenRouterClient = Depends(get_openrouter_client),
) -> ChatUseCase:
    """Dependency для бизнес-логики чата с LLM."""
    return ChatUseCase(chat_repo, client)


def get_current_user_id(
    token: str = Depends(oauth2_scheme),
) -> int:
    """Dependency для получения текущего пользователя из JWT."""
    try:
        payload = decode_token(token)
        user_id = payload.get("sub")

        if user_id is None:
            raise ValueError()

        return int(user_id)

    except Exception:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired token",
        )