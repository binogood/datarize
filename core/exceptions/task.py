from core.exceptions.base import CustomException


class TaskNotFoundException(CustomException):
    code = 404
    error_code = 30001
    message = "Task not found"

