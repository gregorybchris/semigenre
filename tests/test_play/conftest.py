"""Test configuration for semigenre.play tests."""
import os
import pytest

from unittest.mock import MagicMock

from semigenre.play.library import Library


@pytest.fixture(scope='session')
def small_library():
    """Test fixture for a Library object."""
    # TODO: Make this path work from any directory
    filename = os.path.join(os.path.dirname(__file__), 'data', 'library.xml')
    return Library(filename)


@pytest.fixture(scope='session')
def playable_track():
    """Test fixture for a Track object."""
    track = MagicMock()
    track.location = './tests/test_play/data/track.mp3'
    return track
