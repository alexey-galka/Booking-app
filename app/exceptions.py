from fastapi import HTTPException, status


class BookingException(HTTPException):
    status_code = 500,
    detail = ''

    def __init__(self):
        super().__init__(status_code=self.status_code, detail=self.detail)


class UserAlreadyExistsException(BookingException):
    status_code = status.HTTP_409_CONFLICT,
    detail = "User is already exist"


class IncorrectEmailOrPasswordException(BookingException):
    status_code = status.HTTP_401_UNAUTHORIZED,
    detail = "Incorrect email or password"


class ExpiredTokenException(BookingException):
    status_code = status.HTTP_403_FORBIDDEN,
    detail = "Token is expired"


class NoTokenException(BookingException):
    status_code = status.HTTP_401_UNAUTHORIZED,
    detail = "No token"


class IncorrectTokenFormatException(BookingException):
    status_code = status.HTTP_403_FORBIDDEN,
    detail = "Incorrect token format"


class UserNotFoundException(BookingException):
    status_code = status.HTTP_401_UNAUTHORIZED,
