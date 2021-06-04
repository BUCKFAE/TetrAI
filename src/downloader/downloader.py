from pytube import YouTube
from pytube.exceptions import *

class Downloader:

    def _download_video(self, url: str) -> bool:

        print(f"Downloadig video: {url}")

        try:
            # Downloading the video
            YouTube(url).streams.order_by('resolution').desc().first().download("data/videos")

        except:
            print(f"Could not download video: {url}")
            return False

        return True

    def download_videos(self) -> bool:
        
        # Fetches all Videos
        urls = open("src/downloader/urls.txt", "r").readlines()

        print(f"Videos: {urls}")

        # TODO: Exchange this for actual videos
        return self._download_video("https://www.youtube.com/watch?v=e69XZJ9DEj0")