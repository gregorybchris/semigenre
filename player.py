import audio_utilities
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame

from dataclasses import dataclass
from multiprocessing import Process, Pipe
from urllib.parse import urlparse, unquote


@dataclass
class PlayerConfig:
    frequency: int = 44100
    bitsize: int = -16
    channels: int = 2
    buffer: int = 2048
    volume: int = 0.8
    convert: bool = False


class Player:
    PLAY = 'PLAY'
    PAUSE = 'PAUSE'
    STOP = 'STOP'
    FORWARD = 'FORWARD'
    REWIND = 'REWIND'

    def __init__(self, track):
        self._track = track
        self._state = Player.PAUSE
        self._start_time = 0

    def play(self, config: PlayerConfig = None) -> None:
        if config is None:
            config = PlayerConfig()

        self._state = Player.PLAY
        self._pipe, child_pipe = Pipe()
        filename = self._parse_location(self._track.location)
        if config.convert:
            filename = self._convert(filename)
        args = (child_pipe, filename, config)
        p = Process(target=self._play, args=args)
        p.start()
        # TODO: Check what process clean up is needed
        # p.join()

    def _convert(self, filename):
        track_title = self._track.name
        new_filename = os.path.join('./data', 'tracks', track_title + '.mp3')
        audio_utilities.clean_mp3(filename, new_filename)
        return new_filename

    def _parse_location(self, location):
        parser = urlparse(unquote(location))
        return os.path.abspath(os.path.join(parser.netloc, parser.path))

    def _play(self, pipe, filename, config):
        pygame.mixer.init(config.frequency, config.bitsize, config.channels, config.buffer)
        pygame.mixer.music.set_volume(config.volume)
        pygame.mixer.music.load(filename)
        pygame.mixer.music.play()

        clock = pygame.time.Clock()
        while pygame.mixer.music.get_busy():
            if pipe is not None:
                try:
                    signal = pipe.recv()
                except OSError:
                    break
                if signal is not None:
                    if signal[0] == Player.PLAY:
                        pygame.mixer.music.unpause()
                    elif signal[0] == Player.PAUSE:
                        pygame.mixer.music.pause()
                    elif signal[0] == Player.STOP:
                        pipe.close()
                    elif signal[0] == Player.FORWARD:
                        self._start_time = pygame.mixer.music.get_pos() / 1000 + self._start_time + 5
                        pygame.mixer.music.play(0, self._start_time)
                    elif signal[0] == Player.REWIND:
                        self._start_time = pygame.mixer.music.get_pos() / 1000 + self._start_time - 5
                        pygame.mixer.music.play(0, self._start_time)
            clock.tick(30)

    def pause(self) -> None:
        # TODO: Check for a broken pipe when song is done playing
        self._state = Player.PAUSE
        self._pipe.send([Player.PAUSE])
    
    def resume(self) -> None:
        self._state = Player.PLAY
        self._pipe.send([Player.PLAY])

    def stop(self) -> None:
        self._state = Player.STOP
        self._pipe.send([Player.STOP])

    def forward(self) -> None:
        self._pipe.send([Player.FORWARD])

    def rewind(self) -> None:
        self._pipe.send([Player.REWIND])

    def get_state(self) -> str:
        return self._state
