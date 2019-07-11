def test_find_one(small_library):
    track = small_library.find_one(lambda t: 'Alone in' in t.name)
    assert track.artist == 'Air'


def test_find_all(small_library):
    tracks = small_library.find_all(lambda t: 'in' in t.name)
    assert len(tracks) == 2
