import cv2
import numpy as np

from webcam import Camera  # Assuming your camera class is in a 'camera.py' file
from image_processor import processor
from visualizer import visualizer
from logger import logger
from audio_output import audio_out

def main():
    camera_id = 1  # You can change this to the appropriate camera ID (0, 1, 2, etc.) as needed
    cam = Camera(camera_id)
    imgprocessor = processor()
    overlay_visualizer= visualizer()
    logging = logger()
    talker = audio_out()
    

    while True:
        img = cam.get_frame()
        cv2.imshow('Camera Feed', img) #frame
        imgprocessor.detect_shapes(img)

        overlay_visualizer.get_imgdata(imgprocessor.imgdata)
        overlay_visualizer.show_overlay()
        logging.get_imgdata(imgprocessor.imgdata)
        talker.text_to_speech(imgprocessor.imgdata)

        key = cv2.waitKey(1)
        if key == 27:
            break
    

    logging.export()
    #cam.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
