import pytest

from unittest.mock import MagicMock

from semigenre.play.library import Library


@pytest.fixture(scope='session')
def small_library():
    # TODO: Make this path work from any directory
    library_file = './tests/test_play/data/library.xml'
    return Library(library_file)


@pytest.fixture(scope='session')
def playable_track():
    track = MagicMock()
    track.location = './tests/test_play/data/track.mp3'
    return track
