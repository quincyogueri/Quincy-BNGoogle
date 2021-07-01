"""A video playlist class."""

from .video_library import VideoLibrary

class Playlist:
    """A class used to represent a Playlist."""
     def __init__(self, playlist_name: str):
        self._video_library = VideoLibrary()