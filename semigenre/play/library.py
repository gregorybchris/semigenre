"""Library for searching through personal music."""
import plistlib

from semigenre.play.track import TrackFactory


class Library:
    """Library for searching through personal music."""

    TRACKS = 'Tracks'

    def __init__(self, filename, binary=False):
        """
        Construct a Library.

        :param filename: Path to the library.xml file.
        """
        with open(filename, 'rb') as f:
            self._library = plistlib.load(f)
        self._tracks = self._parse_tracks()

    def _parse_tracks(self):
        records = self._library[Library.TRACKS]
        return [TrackFactory.create(record) for _, record in records.items()]

    def find_all(self, predicate):
        """
        Find all matching tracks in the library.

        :param predicate: Function that takes a track and returns True/False.
        :return: List of tracks that satisfy the predicate.
        """
        return [track for track in self._tracks if predicate(track)]

    def find_one(self, predicate):
        """
        Find a matching tracks from the library.

        :param predicate: Function that takes a track and returns True/False.
        :return: One track from the library that satisfies the predicate.
        """
        for track in self._tracks:
            if predicate(track):
                return track
