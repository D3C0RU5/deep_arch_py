from src.utils.requests import InvalidResquest
from src.utils.responses import (
    ResponseFailure,
    ResponseSuccess,
    ResponseType,
    build_invalid_response,
)


SUCCESS_VALUE = {"key": ["value1", "value2"]}
GENERIC_RESPONSE_TYPE = "Response"
GENERIC_RESPONSE_MESSAGE = "This is a response"


class TestResponseSuccess:
    def test_is_true(self):
        response = ResponseSuccess(SUCCESS_VALUE)

        assert bool(response) is True

    def test_has_type_and_message(self):
        response = ResponseSuccess(SUCCESS_VALUE)

        assert response.type == ResponseType.SUCCESS
        assert response.value == SUCCESS_VALUE


class TestResponseFailure:
    def test_is_false(self):
        response = ResponseFailure(GENERIC_RESPONSE_TYPE, GENERIC_RESPONSE_MESSAGE)

        assert bool(response) is False

    def test_has_type_and_message(self):
        response = ResponseFailure(GENERIC_RESPONSE_TYPE, GENERIC_RESPONSE_MESSAGE)

        assert response.type == GENERIC_RESPONSE_TYPE
        assert response.message == GENERIC_RESPONSE_MESSAGE
        assert response.value == {
            "type": GENERIC_RESPONSE_TYPE,
            "message": GENERIC_RESPONSE_MESSAGE,
        }

    def test_initialisation_with_exception(self):
        response = ResponseFailure(
            GENERIC_RESPONSE_TYPE, Exception("Just an error message")
        )

        assert bool(response) is False
        assert response.type == GENERIC_RESPONSE_TYPE
        assert response.message == "Exception: Just an error message"


class TestBuildInvalidResponse:
    def test_response(self):
        request = InvalidResquest()

        request.add_error(parameter="any_value", message="any message")

        response_failure = build_invalid_response(request)

        assert bool(response_failure) is False
        assert response_failure.message == "any_value: any message"
