import os

from music import Song
from player import Player
from pydub import AudioSegment


def play_music(data_dir, music_file):
    print("Playing: ", music_file)
    filepath = os.path.join(data_dir, music_file)
    song = Song(filepath)
    p = Player(song)
    p.play()

    print("Press ENTER to pause and resume")
    playing = True
    while True:
        input("State: {}".format(p.get_state()))
        p.pause() if playing else p.resume()
        playing = not playing


def convert_m4a_to_mp3(filename_in, filename_out):
    sound = AudioSegment.from_file(filename_in, format="m4a")
    sound.export(filename_out, format="mp3")


def clean_mp3(filename):
    sound = AudioSegment.from_file(filename, format="mp3")
    sound.export(filename, format="mp3")


if __name__ == '__main__':
    # music_file = 'Someone Like You.mp3'
    music_file = 'Near To You.mp3'
    # music_file = 'Alone in Kyoto.mp3'
    music_file = 'Shock.mp3'
    # convert_m4a_to_mp3('./data/No One.m4a', './data/No One.mp3')
    music_file = 'No One.mp3'
    music_file = 'Goin Back to Hogwarts.mp3'
    clean_mp3('./data/' + music_file)

    data_dir = './data'
    play_music(data_dir, music_file)