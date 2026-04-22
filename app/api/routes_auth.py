from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm

from app.api.deps import get_auth_usecase, get_current_user_id
from app.usecases.auth import AuthUseCase
from app.schemas.auth import RegisterRequest, TokenResponse
from app.schemas.user import UserPublic
from app.core.errors import ConflictError, UnauthorizedError, NotFoundError


router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/register", response_model=UserPublic)
async def register(
    data: RegisterRequest,
    usecase: AuthUseCase = Depends(get_auth_usecase),
):
    """
    Регистрация нового пользователя.
    """
    try:
        user = await usecase.register(
            email=data.email,
            password=data.password,
        )
        return user

    except ConflictError as e:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=str(e),
        )


@router.post("/login", response_model=TokenResponse)
async def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    usecase: AuthUseCase = Depends(get_auth_usecase),
):
    """
    Аутентификация пользователя и получение JWT токена.
    """
    try:
        token = await usecase.login(
            email=form_data.username,
            password=form_data.password,
        )

        return {
            "access_token": token,
            "token_type": "bearer",
        }

    except UnauthorizedError as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=str(e),
        )


@router.get("/me", response_model=UserPublic)
async def me(
    user_id: int = Depends(get_current_user_id),
    usecase: AuthUseCase = Depends(get_auth_usecase),
):
    """
    Получение профиля текущего пользователя.
    """
    try:
        return await usecase.get_profile(user_id)

    except NotFoundError as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(e),
        )