"""Test configuration for semigenre.rating tests."""
import pytest

from semigenre.cli.format_printer import FormatPrinter


@pytest.fixture(scope='session', params=FormatPrinter.COLORS)
def color(request):
    """Test fixture for all colors."""
    return request.param
