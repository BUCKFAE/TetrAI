from logging import currentframe
from typing import Tuple
import cv2
import os
import re

import numpy as np
import matplotlib.pyplot as plt
import pytesseract


class Importer:

    def __init__(self) -> None:
        """Loads the coordinates"""

        # Reading coordinates, removing everything but numbers as well as player id
        coordinates = open("src/downloading/coordinates.txt", "r").readlines()
        coordinates = [re.sub("[^0-9]", "", c) for c in coordinates]
        coordinates = [int(c[1:]) for c in coordinates if c]

        # Coordinates game player 1
        self.p1_game_start = (coordinates[0], coordinates[1])
        self.p1_game_end = (coordinates[2], coordinates[3])

        # Coordinates game player 2
        self.p2_game_start = (coordinates[4], coordinates[5])
        self.p2_game_end = (coordinates[6], coordinates[7])

        # Coordinates name player 1
        self.p1_name_start = (coordinates[8], coordinates[9])
        self.p1_name_end = (coordinates[10], coordinates[11])

        # Coordinates name player 2
        self.p2_name_start = (coordinates[12], coordinates[13])
        self.p2_name_end = (coordinates[14], coordinates[15])


    def import_video(self, url: str) -> bool:

        url = os.getcwd() + url

        print(f"Downloadig video: {url}")

        print("file exists?", os.path.exists(url))

        cam = cv2.VideoCapture(url)
        cam.set(cv2.cv2.CAP_PROP_POS_FRAMES, 17 * 60 * 30)
        


        while(True):
            
            # Getting current frame
            foundFrame, frame = cam.read()


            print(f"Type: {type(frame)}")

            if foundFrame:

                # res = self._check_if_frame_contains_gameplay(frame)
                res = self._extract_player_names_from_frame(frame)
                #img = plt.imshow(frame)

                #plt.savefig("Test.png")
            else:
                break

            break
        
        # Release the cam
        cam.release()


    def _check_if_frame_contains_gameplay(self, frame: np.ndarray) -> bool:

        img = plt.imshow(frame)
        plt.show()

        start_x = 611
        start_y = 275

        end_x = 925
        end_y = 890

        # Array 1080 1920
        frame = frame[start_y:end_y, start_x:end_x]

        pass

    def _extract_player_names_from_frame(self, frame: np.ndarray):

        print(f"{self.p1_name_start[1]}:{self.p1_name_end[1]}, {self.p1_name_start[0]}:{self.p1_name_end[0]}")


        img_p1_name = frame[self.p1_name_start[1]:self.p1_name_end[1], self.p1_name_start[0]:self.p1_name_end[0]]
        img_p1_name = np.invert(img_p1_name)

        img_p2_name = frame[self.p2_name_start[1]:self.p2_name_end[1], self.p2_name_start[0]:self.p2_name_end[0]]
        img_p2_name = np.invert(img_p2_name)

        name1 = pytesseract.image_to_string(img_p1_name, config="--oem 3 --psm 7")
        name2 = pytesseract.image_to_string(img_p2_name, config="--oem 3 --psm 7")

        # Removing everything but letters
        name1 = re.sub("[^A-Z]", "", name1)
        name2 = re.sub("[^A-Z]", "", name2)

        print(f"Player 1: \"{name1}\"\nPlayer2: \"{name2}\"")

        # Showing the name as plot
        img = plt.imshow(img_p1_name)
        plt.show()
        img = plt.imshow(img_p2_name)
        plt.show()