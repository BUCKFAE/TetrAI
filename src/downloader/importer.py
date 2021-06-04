from logging import currentframe
import cv2
import os

import matplotlib.pyplot as plt


class Importer:

    def import_video(self, url: str) -> bool:

        print("file exists?", os.path.exists(url))

        cam = cv2.VideoCapture(url)
        
        skip_first = 10 * 60 * 30
        current_frame = 0

        while(True):
            
            if current_frame < skip_first:
                current_frame += 100
                continue


            # Getting current frame
            foundFrame, frame = cam.read()
        
            if foundFrame:
                img = plt.imshow(frame)
                plt.show()
            else:
                break
        
        # Release the cam
        cam.release()
