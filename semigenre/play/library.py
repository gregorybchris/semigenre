import plistlib

from semigenre.play.track import TrackFactory


class Library:
    TRACKS = 'Tracks'

    def __init__(self, filename, binary=False):
        with open(filename, 'rb') as f:
            self._library = plistlib.load(f)
        self._tracks = self._parse_tracks()

    def _parse_tracks(self):
        track_records = self._library[Library.TRACKS]
        return [TrackFactory.create(record) for _, record in track_records.items()]

    def get_random(self):
        return self._tracks[32]

    def find_all(self, predicate):
        return [track for track in self._tracks if predicate(track)]

    def find_one(self, predicate):
        for track in self._tracks:
            if predicate(track):
                return track
