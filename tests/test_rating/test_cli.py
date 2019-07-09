from unittest.mock import MagicMock, patch

from semigenre.rating import cli


class MockCLI:
    def __init__(self, responses):
        self._responses = responses

    def __call__(self, prompt):
        return self._responses.pop(0)


@patch('builtins.input', MockCLI(['Chris', 'yes']))
def test_run_yes():
    library_mock = MagicMock()
    rating_cli = cli.RatingCLI(library_mock)
    rating_cli.run()


@patch('builtins.input', MockCLI(['Chris', 'no']))
def test_run_no():
    library_mock = MagicMock()
    rating_cli = cli.RatingCLI(library_mock)
    rating_cli.run()
