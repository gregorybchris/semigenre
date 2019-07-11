from unittest.mock import MagicMock, patch

from semigenre.rating import rating_cli


class MockCLI:
    def __init__(self, responses):
        self._responses = responses

    def __call__(self, prompt):
        return self._responses.pop(0)


@patch('builtins.input', MockCLI(['Chris', 'q']))
def test_run():
    library_mock = MagicMock()
    cli = rating_cli.RatingCLI(library_mock)
    cli.run()
