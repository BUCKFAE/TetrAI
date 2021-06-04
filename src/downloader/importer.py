import cv2

import matplotlib.pyplot as plt


class Importer:

    def import_video(self, url: str) -> bool:

        cam = cv2.VideoCapture(url)
        
        while(True):
            
            # Getting current frame
            foundFrame, frame = cam.read()
        
            if foundFrame:
                img = plt.imshow(frame)
                plt.show()
            else:
                break
        
        # Release the cam
        cam.release()
