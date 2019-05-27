from library import Library
from player import Player


def play_track(track):
    print("Playing: ", track.name)

    p = Player(track)
    p.play()

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
        elif signal == 'r':
            p.rewind()


if __name__ == '__main__':
    library_file = './data/library.xml'
    library = Library(library_file)
    # track = library.find_one(lambda t: 'Jesu Joy' in t.name) # Works
    # track = library.find_one(lambda t: "Shock" in t.name) # Works
    track = library.find_one(lambda t: "Goin' Back to Hogwarts" in t.name) # Faulty mp3
    # track = library.find_one(lambda t: "No One" in t.name) # Only m4a

    play_track(track)