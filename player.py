import os

from music import Song
from multiprocessing import Process, Pipe


class Player:
    def __init__(self, song):
        self._song = song
        self._state = Song.PAUSE

    def _play_song(self, song, pipe):
        song.play(pipe=pipe)

    def play(self):
        self._state = Song.PLAY
        self._song_pipe, child_pipe = Pipe()
        args = (self._song, child_pipe)
        p = Process(target=self._play_song, args=args)
        p.start()
        # p.join()

    def pause(self):
        self._state = Song.PAUSE
        self._song_pipe.send([Song.PAUSE])
    
    def resume(self):
        self._state = Song.PLAY
        self._song_pipe.send([Song.PLAY])

    def get_state(self):
        return self._state
