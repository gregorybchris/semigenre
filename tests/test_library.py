from semigenre.play.library import Library


def test_library():
    library_file = './test_data/library.xml'
    library = Library(library_file)
    track = library.find_one(lambda t: 'Jesu Joy' in t.name)
    assert track.artist == 'Academy of St. Martin in the Fields'
