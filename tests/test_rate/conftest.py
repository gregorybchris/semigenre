import pytest

from semigenre.rate import tags


@pytest.fixture(scope='session', params=tags.ALL)
def tag_name(request):
    """Test fixture for all tags."""
    return request.param
