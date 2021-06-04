import os

from pytube import YouTube
from pytube.exceptions import *

class Downloader:

    def _download_video(self, url: str) -> bool:

        try:
            # Downloading the video
            streams = YouTube(url).streams.order_by('resolution').filter(mime_type="video/webm").desc()

            for s in streams:
                print(s)

            streams.first().download("data/videos", "vid")

        except:
            print(f"Could not download video: {url}")
            return False

        return True

    def download_videos(self) -> bool:
        
        # Fetches all Videos
        urls = open("src/downloader/urls.txt", "r").readlines()


        # TODO: Ensure Video URLS are correct
        print(f"Videos: {urls}")

        # TODO: Exchange this for actual videos
        return self._download_video("https://www.youtube.com/watch?v=L_UPHsGR6fM")