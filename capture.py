

from cv2 import cv2


class Capture:

    def __init__(self,filename):
        cam = cv2.VideoCapture(0)

        cv2.namedWindow("test")

        img_counter = 0

        while True:
            ret, frame = cam.read()
            cv2.imshow("test", frame)
            if not ret:
                break
            
            # SPACE pressed
            img_name = "{}.png".format(filename)
            cv2.imwrite(img_name, frame)
            

            cam.release()
            break

        cv2.destroyAllWindows()