import re


def test_tags_format(tag_name):
    tag_pattern = r'[0-9a-zA-Z\-]{3,15}'
    m = re.match(tag_pattern, tag_name)
    assert m is not None
