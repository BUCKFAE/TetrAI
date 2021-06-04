import unittest

from src.downloader.importer import Importer


class Test_Importer(unittest.TestCase):

    def test_import(self):
        importer = Importer().import_video("C:\\Users\\infor\\Documents\\DeepLearning\\TetrAI\\data\\videos\\The Sun Sneeze Gene.webm")
