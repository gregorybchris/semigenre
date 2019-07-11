"""Test configuration for semigenre.cli tests."""
import pytest

from semigenre.cli.format_io import FormatIO


@pytest.fixture(scope='session', params=FormatIO.COLORS)
def color(request):
    """Test fixture for all colors."""
    return request.param
