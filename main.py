from music import Song
from player import Player


def play_music(music_file):
    song = Song(music_file)
    p = Player(song)
    p.play()

    playing = True
    print("Music playing...")
    print("Press ENTER to pause and resume")
    while True:
        input("State: {}\n".format(p.get_state()))
        p.pause() if playing else p.resume()
        playing = not playing


if __name__ == '__main__':
    music_file = './data/Alone in Kyoto.mp3'
    play_music(music_file)