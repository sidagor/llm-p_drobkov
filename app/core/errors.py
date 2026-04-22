class AppError(Exception):
    """Базовая ошибка приложения"""
    pass


class ConflictError(AppError):
    """Конфликт (например, email уже существует)"""
    pass


class UnauthorizedError(AppError):
    """Неавторизован (неверные данные)"""
    pass


class ForbiddenError(AppError):
    """Запрещено (нет прав доступа)"""
    pass


class NotFoundError(AppError):
    """Не найдено (объект отсутствует)"""
    pass


class ExternalServiceError(AppError):
    """Ошибка внешнего сервиса (например, OpenRouter)"""
    pass