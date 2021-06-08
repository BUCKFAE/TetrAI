import unittest

from src.downloading.downloader import Downloader


class Test_Downloader(unittest.TestCase):

    def test_download(self):
        downloader = Downloader().download_videos()
