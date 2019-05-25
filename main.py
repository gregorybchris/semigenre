from library import Library
from player import Player, PlayerConfig


def play_track(track):
    print("Playing: ", track.name)

    config = PlayerConfig(convert=False)
    p = Player(track)
    p.play(config=config)

    print("Press ENTER to pause and resume")
    playing = True
    while True:
        signal = input("State: {}".format(p.get_state()))
        if signal == 's':
            p.stop()
            break
        elif signal == 'p':
            p.pause() if playing else p.resume()
            playing = not playing
        elif signal == 'f':
            p.forward()
        elif signal == 'b':
            p.rewind()


if __name__ == '__main__':
    ['Someone Like You', 'Near To You', 'Shock', 'No One', 'Goin Back to Hogwarts']

    library_file = './data/library.xml'
    library = Library(library_file)
    # track = library.find_one(lambda t: 'Hogwarts' in t.name)
    track = library.find_one(lambda t: 'Joy' in t.name)
    play_track(track)