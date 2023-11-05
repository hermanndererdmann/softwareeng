import cv2

from webcam import Camera  # Assuming your camera class is in a 'camera.py' file
from image_processor import processor
from visualizer import visualizer
from logger import logger
from audio_output import audio_out

def main():
    camera_id = 1  # You can change this to the appropriate camera ID (0, 1, 2, etc.) as needed
    
    #Generate objects
    cam = Camera(camera_id)
    imgprocessor = processor()
    overlay_visualizer= visualizer()
    logging = logger()
    talker = audio_out()
    

    while True:
        #Get Image
        img = cam.get_frame()
        #Process image
        imgprocessor.detect_shapes(img)
        #Generate and show overlay
        overlay_visualizer.get_imgdata(imgprocessor.imgdata)
        overlay_visualizer.show_overlay()
        #Logging the seen data
        logging.get_imgdata(imgprocessor.imgdata)
        #Audio output
        talker.text_to_speech(imgprocessor.imgdata)

        key = cv2.waitKey(1)
        if key == 27:
            break
    
    #Safe the collected data in a .csv
    logging.export()
    #Release cam and close windows
    cam.release_camera()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
