"""A playlist class."""


class Playlist:
    """A class used to represent a Video."""

    def __init__(self, playlist_name: str, video_id:[]):
        """playlist constructor."""
        self._name = playlist_name
        self._video_id = video_id

    @property
    def name(self) -> str:
        """Returns the name of a playlist."""
        return self._name

    @property
    def video_id(self) -> []:
        """Returns the video id of a video."""
        return self._video_id

