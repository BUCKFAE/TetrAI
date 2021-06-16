import os
import sys
import unittest

sys.path.append(os.getcwd())

from src.downloading.importer import Importer


class Test_Importer(unittest.TestCase):

    def test_import(self):
        importer = Importer().import_video("/data/videos/vid.webm")
        pass

if __name__ == "__main__":
    print(os.getcwd())
    unittest.main()
