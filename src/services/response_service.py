import json


class Response:

    def __init__(self, status_code: int, message: str, meta: dict = None):
        self.status_code = status_code
        self.message = message
        self.meta = meta
        if not meta:
            self.meta = {}

    def get_response(self) -> dict:
        return {
            "code": self.status_code,
            "message": self.message,
            "meta": self.meta
        }
