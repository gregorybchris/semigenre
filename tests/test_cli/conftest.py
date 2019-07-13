"""Test configuration for semigenre.cli tests."""
import pytest

from semigenre.cli.color import Color


@pytest.fixture(scope='session', params=Color.ALL)
def color(request):
    """Test fixture for all colors."""
    return request.param
