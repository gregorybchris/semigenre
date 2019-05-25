import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
import time


class Song:
    PLAY = 'PLAY'
    PAUSE = 'PAUSE'

    FREQUENCY = 44100
    BITSIZE = -16
    CHANNELS = 2
    BUFFER = 2048

    def __init__(self, filename):
        self._filename = filename

    def play(self, volume=0.8, pipe=None):
        pygame.mixer.init(Song.FREQUENCY, Song.BITSIZE, Song.CHANNELS, Song.BUFFER)
        pygame.mixer.music.set_volume(volume)
        pygame.mixer.music.load(self._filename)
        pygame.mixer.music.play()

        clock = pygame.time.Clock()
        while pygame.mixer.music.get_busy():
            if pipe is not None:
                signal = pipe.recv()
                if signal is not None:
                    if signal[0] == Song.PLAY:
                        pygame.mixer.music.unpause()
                    elif signal[0] == Song.PAUSE:
                        pygame.mixer.music.pause()
            clock.tick(30)
