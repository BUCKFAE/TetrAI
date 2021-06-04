from logging import currentframe
import cv2
import os

import numpy as np
import matplotlib.pyplot as plt


class Importer:

    def import_video(self, url: str) -> bool:

        url = os.getcwd() + url

        print(f"Downloadig video: {url}")

        print("file exists?", os.path.exists(url))

        cam = cv2.VideoCapture(url)
        cam.set(cv2.cv2.CAP_PROP_POS_FRAMES, 17 * 60 * 30)
        


        while(True):
            
            # Getting current frame
            foundFrame, frame = cam.read()

            start_x = 611
            start_y = 275

            end_x = 925
            end_y = 890

            # Array 1080 1920
            frame = frame[start_y:end_y, start_x:end_x]


            if foundFrame:
                img = plt.imshow(frame)
                plt.show()
            else:
                break
        
        # Release the cam
        cam.release()
