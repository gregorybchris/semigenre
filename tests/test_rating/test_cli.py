from unittest.mock import MagicMock, patch

from semigenre.rating.cli import RatingCLI


class MockCLIInput:
    def __init__(self, responses):
        self._responses = responses

    def __call__(self, prompt):
        return self._responses.pop(0)


class MockCLIPrint:
    def __init__(self):
        pass

    def __call__(self, message=None, end=None):
        pass


@patch('builtins.print', MockCLIPrint())
@patch('builtins.input', MockCLIInput(['Chris', 't', 'q', 'y']))
def test_run_tag():
    library_mock = MagicMock()
    cli = RatingCLI(library_mock)
    cli.run()


@patch('builtins.print', MockCLIPrint())
@patch('builtins.input', MockCLIInput(['Chris', 'c', 'q', 'y']))
def test_run_compare():
    library_mock = MagicMock()
    cli = RatingCLI(library_mock)
    cli.run()


@patch('builtins.print', MockCLIPrint())
@patch('builtins.input', MockCLIInput(['Chris', 'h', 'q', 'y']))
def test_run_help():
    library_mock = MagicMock()
    cli = RatingCLI(library_mock)
    cli.run()
