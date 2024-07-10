class POSBaseException(Exception):

    code = 500

    def __init__(self, message: str, errors: dict | None = None):
        self.message = message
        self.errors = errors


class POSValidationException(POSBaseException):

    code = 400


class POSNotFoundException(POSBaseException):

    code = 404
