import cv2
import numpy as np

from webcam import Camera  # Assuming your camera class is in a 'camera.py' file
from image_processor import processor

def main():
    camera_id = 1  # You can change this to the appropriate camera ID (0, 1, 2, etc.) as needed
    cam = Camera(camera_id)
    imgprocessor = processor()


    while True:
        img = cam.get_frame()
        cv2.imshow('Camera Feed', img) #frame
        imgprocessor.detect_shapes(img)


        key = cv2.waitKey(1)
        if key == 27:
            break

    cam.release()
    #cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
