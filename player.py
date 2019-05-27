import os
import time
import vlc

from multiprocessing import Process, Pipe
from urllib.parse import urlparse, unquote


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

    def play(self) -> None:
        self._state = Player.PLAY
        self._pipe, child_pipe = Pipe()
        filepath = self._parse_location(self._track.location)
        args = (child_pipe, filepath)
        p = Process(target=self._play, args=args)
        p.start()
        # TODO: Check what process clean up is needed
        # p.join()

    def _parse_location(self, location):
        parser = urlparse(unquote(location))
        return os.path.abspath(os.path.join(parser.netloc, parser.path))

    def _play(self, pipe, filepath):
        vlc_instance = vlc.Instance()
        vlc_player = vlc_instance.media_player_new()
        media = vlc_instance.media_new(filepath)
        vlc_player.set_media(media)
        vlc_player.play()
        time.sleep(.5)

        while True:
            if pipe is not None:
                try:
                    signal = pipe.recv()
                except OSError:
                    break
                except KeyboardInterrupt:
                    break
                if signal is not None:
                    if signal[0] == Player.PLAY:
                        vlc_player.play()
                    elif signal[0] == Player.PAUSE:
                        vlc_player.pause()
                    elif signal[0] == Player.STOP:
                        pipe.close()
                        break
                    elif signal[0] == Player.FORWARD:
                        vlc_player.set_position(vlc_player.get_position() + 0.05)
                    elif signal[0] == Player.REWIND:
                        vlc_player.set_position(vlc_player.get_position() - 0.05)
                        pass
            time.sleep(1)

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
