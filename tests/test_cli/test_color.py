from semigenre.cli.color import Color


def test_get_color():
    all_names = {'blue', 'green', 'red', 'yellow',
        'magenta', 'cyan', 'white', 'purple'}

    assert len(all_names) == len(Color.ALL)
    for name in all_names:
        assert Color.get(name) in Color.ALL
