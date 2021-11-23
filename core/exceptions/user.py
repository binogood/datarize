from core.exceptions.base import CustomException


class DuplicateEmailException(CustomException):
    code = 400
    error_code = 20000
    message = "duplicate email"


class UserNotFoundException(CustomException):
    code = 404
    error_code = 20001
    message = "User not found"

