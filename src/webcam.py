import cv2

class Camera:
    def __init__(self,camera_id):
        self.cap = cv2.VideoCapture(camera_id)

        # Set the desired FPS (30 FPS)
        self.cap.set(cv2.CAP_PROP_FPS, 30)

    def get_frame(self):
        s, img = self.cap.read()
        try: 
            if s:  # frame captures without errors
                return img
            return None
        except ValueError: 
            return 'Error'

    def release_camera(self):
        #release cam
        self.cap.release()

