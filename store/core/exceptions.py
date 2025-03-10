class BaseException(Exception):
    message: str = "Internal Server  Error"

    def __init__(self, *args: object, message: str | None = None) -> None:
        super().__init__(*args)
        if message:
            self.message = message


class NotFoundExcpection(BaseException):
    message = "Not Found"
