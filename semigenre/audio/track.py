"""Music track DTO."""
from dataclasses import dataclass
from datetime import datetime


@dataclass
class Track:
    """Music track DTO."""

    album: str
    album_artist: str
    album_rating: int
    album_rating_computed: bool
    artist: str
    artwork_count: int
    bit_rate: int
    bpm: int
    clean: bool
    comments: str
    compilation: bool
    composer: str
    content_rating: str
    date_added: datetime
    date_modified: datetime
    disc_count: int
    disc_number: int
    episode: str
    episode_order: int
    explicit: bool
    file_folder_count: int
    file_type: int
    genre: str
    grouping: str
    has_video: bool
    kind: str
    library_folder_count: int
    location: str
    movie: bool
    name: str
    persistent_id: str
    play_count: int
    play_date: int
    play_date_utc: datetime
    podcast: bool
    protected: bool
    purchased: bool
    rating: int
    release_date: datetime
    sample_rate: int
    season: int
    series: str
    size: int
    skip_count: int
    skip_date: datetime
    sort_album: str
    sort_album_artist: str
    sort_artist: str
    sort_composer: str
    sort_name: str
    start_time: int
    stop_time: int
    total_time: int
    track_count: int
    track_id: int
    track_number: int
    track_type: str
    tv_show: bool
    unplayed: bool
    volume_adjustment: int
    work: str
    year: int


class TrackFactory:
    """Factory for Tracks."""

    @staticmethod
    def create(d: dict) -> Track:
        """
        Create a track based on a dictionary of track attributes.

        :param d: A dictionary containing the track attributes.
        :return: A new Track object based on d.
        """
        properties = ['Album', 'Album Artist', 'Album Rating',
                      'Album Rating Computed', 'Artist', 'Artwork Count',
                      'BPM', 'Bit Rate', 'Clean', 'Comments', 'Compilation',
                      'Composer', 'Content Rating', 'Date Added',
                      'Date Modified', 'Disc Count', 'Disc Number', 'Episode',
                      'Episode Order', 'Explicit', 'File Folder Count',
                      'File Type', 'Genre', 'Grouping', 'Has Video', 'Kind',
                      'Library Folder Count', 'Location', 'Movie', 'Name',
                      'Persistent ID', 'Play Count', 'Play Date',
                      'Play Date UTC', 'Podcast', 'Protected', 'Purchased',
                      'Rating', 'Release Date', 'Sample Rate', 'Season',
                      'Series', 'Size', 'Skip Count', 'Skip Date',
                      'Sort Album', 'Sort Album Artist', 'Sort Artist',
                      'Sort Composer', 'Sort Name', 'Start Time', 'Stop Time',
                      'TV Show', 'Total Time', 'Track Count', 'Track ID',
                      'Track Number', 'Track Type', 'Unplayed',
                      'Volume Adjustment', 'Work', 'Year']
        track_args = [d.get(p) for p in properties]
        return Track(*track_args)
