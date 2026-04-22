import httpx

from app.core.config import settings
from app.core.errors import ExternalServiceError


class OpenRouterClient:
    """
    Клиент для взаимодействия с OpenRouter API.
    """

    def __init__(self):
        """
        Инициализация клиента с настройками из конфигурации.
        """
        self._base_url = settings.openrouter_base_url
        self._api_key = settings.openrouter_api_key
        self._model = settings.openrouter_model

    async def chat(
        self,
        messages: list[dict],
        temperature: float = 0.7,
    ) -> str:
        """
        Отправляет запрос в OpenRouter и возвращает ответ модели.
        """
        url = f"{self._base_url}/chat/completions"

        headers = {
            "Authorization": f"Bearer {self._api_key}",
            "HTTP-Referer": settings.openrouter_site_url,
            "X-Title": settings.openrouter_app_name,
            "Content-Type": "application/json",
        }

        payload = {
            "model": self._model,
            "messages": messages,
            "temperature": temperature,
        }

        async with httpx.AsyncClient(timeout=30.0) as client:
            response = await client.post(
                url,
                headers=headers,
                json=payload,
            )

        if response.status_code != 200:
            raise ExternalServiceError(
                f"OpenRouter error: {response.status_code} {response.text}"
            )

        data = response.json()

        try:
            return data["choices"][0]["message"]["content"]
        except (KeyError, IndexError):
            raise ExternalServiceError("Invalid response format from OpenRouter")