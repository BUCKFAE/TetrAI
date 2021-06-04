import unittest

from src.downloader.importer import Importer


class Test_Importer(unittest.TestCase):

    def test_import(self):
        importer = Importer().import_video("/Users/buckfae/Documents/TetrAI/data/videos/vid.mp4")
