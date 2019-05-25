from pydub import AudioSegment


def convert_m4a_to_mp3(filename_in, filename_out):
    sound = AudioSegment.from_file(filename_in, format="m4a")
    sound.export(filename_out, format="mp3")


def clean_mp3(filename_in, filename_out):
    sound = AudioSegment.from_file(filename_in, format="mp3")
    sound.export(filename_out, format="mp3")