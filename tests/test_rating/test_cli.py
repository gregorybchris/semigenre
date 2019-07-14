from unittest.mock import MagicMock, patch

from semigenre.rating.cli import RatingCLI


class MockCLI:
    def __init__(self, responses):
        self._responses = responses

    def __call__(self, prompt):
        return self._responses.pop(0)


@patch('builtins.input', MockCLI(['Chris', 't', 'q']))
def test_run_tag():
    library_mock = MagicMock()
    cli = RatingCLI(library_mock)
    cli.run()


@patch('builtins.input', MockCLI(['Chris', 'c', 'q']))
def test_run_compare():
    library_mock = MagicMock()
    cli = RatingCLI(library_mock)
    cli.run()


@patch('builtins.input', MockCLI(['Chris', 'h', 'q']))
def test_run_help():
    library_mock = MagicMock()
    cli = RatingCLI(library_mock)
    cli.run()
