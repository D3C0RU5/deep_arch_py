class ResponseType:
    PARAMETERS_ERROR = "ParametersError"
    RESOURCES_ERROR = "ResourcesError"
    SYSTEM_ERROR = "SystemError"
    SUCCESS = "Success"


class ResponseFailure:
    def __init__(self, type_, message):
        self.type = type_
        self.message = self._format_message(message)

    def _format_message(self, message):
        if isinstance(message, Exception):
            return "{}: {}".format(message.__class__.__name__, message)

        return message

    @property
    def value(self):
        return {"type": self.type, "message": self.message}

    def __bool__(self):
        return False


class ResponseSuccess:
    def __init__(self, value=None):
        self.type = ResponseType.SUCCESS
        self.value = value

    def __bool__(self):
        return True


def build_invalid_response(invalid_request):
    message = "\n".join(
        [
            "{}: {}".format(err["parameter"], err["message"])
            for err in invalid_request.errors
        ]
    )

    return ResponseFailure(ResponseType.PARAMETERS_ERROR, message)
