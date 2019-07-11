import re

from semigenre.rating import tags


def test_tags_format(tag_name):
    tag_pattern = r'[0-9a-zA-Z\-]{3,15}'
    m = re.match(tag_pattern, tag_name)
    assert m is not None


def test_tag_groups():
    for _, group in tags.TAG_GROUPS.items():
        assert len(group) > 0


def test_groups_contain_all():
    full_set = set()
    for _, group in tags.TAG_GROUPS.items():
        full_set |= group
    assert len(full_set) == len(tags.ALL)
