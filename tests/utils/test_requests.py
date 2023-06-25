from src.utils.requests import InvalidResquest


class TestBuildResponseFromInvalidRequest:
    def test_response(self):
        request = InvalidResquest()

        request.add_error(parameter="any_value",message="any message")
        request.add_error(parameter="any_value",message="any message")

        assert request.has_errors()
        assert len(request.errors) == 2
