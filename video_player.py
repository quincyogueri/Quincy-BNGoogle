"""A video player class."""

from .video_library import VideoLibrary
import random
import os
THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))


class VideoPlayer:
    """A class used to represent a Video Player."""

    def __init__(self):
        self._video_library = VideoLibrary()

    def number_of_videos(self):
        num_videos = len(self._video_library.get_all_videos())
        print(f"{num_videos} videos in the library")

    def show_all_videos(self):
        """Returns all videos."""
        # Approach 1
        print("Here's a list of all available videos:")
        template = "{} ({}) [{}]"
        str_lst = []
        for v in self._video_library.get_all_videos():
            title = v._title
            video_id = v._video_id
            tags_tup = v._tags
            tags_str = " ".join(tags_tup)
            str_lst.append(template.format(title, video_id, tags_str))
        str_lst.sort()
        for s in str_lst:
            print(s)
        # Approach 2 directly read from txt file
        #my_file = os.path.join(THIS_FOLDER, 'videos.txt')
        #f = open(my_file, "r")
        #template = "{} ({}) [{}]"
        #for video in f.readlines():
        #    video_info = video.split("|")
        #    print(template.format(video_info[0].strip(),video_info[1].strip(),video_info[2].strip()))

        #print("show_all_videos needs implementation")
    def all_playing(self):
        "Return video object current playing"
        videos = self._video_library.get_all_videos()
        for v in videos:
            if v._status == 1:
                return(v)
        return(None)

    def all_paused(self):
        "Return video object current playing"
        videos = self._video_library.get_all_videos()
        for v in videos:
            if v._status == 2:
                return(v)
        return(None)

    def play_video(self, video_id):
        """Plays the respective video.

        Args:
            video_id: The video_id to be played.
        """
        video = self._video_library.get_video(video_id)
        if video is None:
            print("Cannot play video: Video does not exist")
        else:
            if self.all_playing() is not None:
                print("Stopping video: {}".format(self.all_playing()._title))
                self.all_playing()._status = 0
            elif self.all_paused() is not None:
                print("Stopping video: {}".format(self.all_paused()._title))
                self.all_paused()._status = 0
            print("Playing video: {}".format(video._title))
            video._status = 1
        #print("play_video needs implementation")

    def stop_video(self):
        """Stops the current video."""
        if self.all_playing() is None:
            print("Cannot stop video: No video is currently playing")
        else:
            print("Stopping video: {}".format(self.all_playing()._title))
            self.all_playing()._status = 0
        #print("stop_video needs implementation")

    def play_random_video(self):
        """Plays a random video from the video library."""
        video = random.choice(self._video_library.get_all_videos())
        self.play_video(video._video_id)
        #print("play_random_video needs implementation")

    def pause_video(self):
        """Pauses the current video."""
        if self.all_paused() is not None:
            print("Video already paused: {}".format(self.all_paused()._title))
        elif self.all_playing() is not None:
            print("Pausing video: {}".format(self.all_playing()._title))
            self.all_playing()._status = 2
        else:
            print("Cannot pause video: No video is currently playing")
        #print("pause_video needs implementation")

    def continue_video(self):
        """Resumes playing the current video."""
        if self.all_playing() is not None:
            print("Cannot continue video: Video is not paused")
        elif self.all_paused() is not None:
            print("Continuing video: {}".format(self.all_paused()._title))
            self.all_paused()._status = 1
        else:
            print("Cannot continue video: No video is currently playing")
        #print("continue_video needs implementation")

    def show_playing(self):
        """Displays video currently playing."""
        if self.all_playing() is not None:
            tup = self.all_playing()._tags
            print("Currently playing: {} ({}) [{}]".format(self.all_playing()._title, self.all_playing()._video_id, " ".join(tup)))
        elif self.all_paused() is not None:
            tup = self.all_paused()._tags
            print("Currently playing: {} ({}) [{}] - PAUSED".format(self.all_paused()._title, self.all_paused()._video_id, " ".join(tup)))
        else:
            print("No video is currently playing")
        #print("show_playing needs implementation")

    def create_playlist(self, playlist_name):
        """Creates a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("create_playlist needs implementation")

    def add_to_playlist(self, playlist_name, video_id):
        """Adds a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be added.
        """
        print("add_to_playlist needs implementation")

    def show_all_playlists(self):
        """Display all playlists."""

        print("show_all_playlists needs implementation")

    def show_playlist(self, playlist_name):
        """Display all videos in a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("show_playlist needs implementation")

    def remove_from_playlist(self, playlist_name, video_id):
        """Removes a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be removed.
        """
        print("remove_from_playlist needs implementation")

    def clear_playlist(self, playlist_name):
        """Removes all videos from a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("clears_playlist needs implementation")

    def delete_playlist(self, playlist_name):
        """Deletes a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("deletes_playlist needs implementation")

    def search_videos(self, search_term):
        """Display all the videos whose titles contain the search_term.

        Args:
            search_term: The query to be used in search.
        """
        print("search_videos needs implementation")

    def search_videos_tag(self, video_tag):
        """Display all videos whose tags contains the provided tag.

        Args:
            video_tag: The video tag to be used in search.
        """
        print("search_videos_tag needs implementation")

    def flag_video(self, video_id, flag_reason=""):
        """Mark a video as flagged.

        Args:
            video_id: The video_id to be flagged.
            flag_reason: Reason for flagging the video.
        """
        print("flag_video needs implementation")

    def allow_video(self, video_id):
        """Removes a flag from a video.

        Args:
            video_id: The video_id to be allowed again.
        """
        print("allow_video needs implementation")
