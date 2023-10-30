import cv2
import numpy as np

from webcam import Camera  # Assuming your camera class is in a 'camera.py' file

def main():
    while True:
        camera_id = 0  # You can change this to the appropriate camera ID (0, 1, 2, etc.) as needed
        cam = Camera(camera_id)
        img = cam.get_frame()
        cv2.imshow('Camera Feed', img) #frame


if __name__ == "__main__":
    main()
