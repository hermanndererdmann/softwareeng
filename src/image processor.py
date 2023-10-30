import cv2
import numpy as np

class ImgData:
    def __init__(self):
        self.img = None
        self.pattern = []
        self.color = []
        self.contour = []
        self.cx = []
        self.cy = []

class image_processor:
    def __init__(self):
        self.imgdata = ImgData()

    def detect_shapes(self, img):
        # setting threshold of gray image 
        self.__gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # Apply Gaussian blur to reduce noise
        self.__blurred = cv2.GaussianBlur(self.__gray, (5, 5), 0)

        # Detect edges using Canny edge detection
        self.__edges = cv2.Canny(self.__blurred, 50, 150)

        # Find contours in the edge image
        contours, _ = cv2.findContours(self.__edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        for contour in contours:
            # Approximate the shape
            epsilon = 0.04 * cv2.arcLength(contour, True)
            approx = cv2.approxPolyDP(contour, epsilon, True)

            # Determine the shape based on the number of vertices
            num_vertices = len(approx)
            if num_vertices == 3:
                self.imgdata.pattern.append("Triangle")
            elif num_vertices == 4:
                # Check the aspect ratio to determine Rectangle or Square
                x, y, w, h = cv2.boundingRect(contour)
                aspect_ratio = float(w) / h
                if 0.95 <= aspect_ratio <= 1.05:
                    self.imgdata.pattern.append("Square")
                else:
                    self.imgdata.pattern.append("Rectangle")
            else:
                self.imgdata.pattern.append("Circle")

            # Calculate the centroid of the contour
            M = cv2.moments(contour)
            cx = int(M['m10'] / M['m00'])
            cy = int(M['m01'] / M['m00'])

            # Store the detected contour information
            self.imgdata.contour.append(contour)
            self.imgdata.cx.append(cx)
            self.imgdata.cy.append(cy)

            # Call detect_colors to detect color around the centroid
            self.detect_colors(img, cx, cy)

    def detect_colors(self, img, cx, cy):
        # Convert the image to the HSV color space
        self.__hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

        # Define color ranges for the specified colors
        color_ranges = {
            'red': [(0, 100, 100), (10, 255, 255)],
            'green': [(35, 100, 100), (85, 255, 255)],
            'blue': [(100, 100, 100), (130, 255, 255)],
            'yellow': [(20, 100, 100), (30, 255, 255)],
            'violet': [(130, 100, 100), (160, 255, 255)],
        }

        # Extract color from a 5x5 region around the centroid (cx, cy)
        color_region = self.__hsv_img[cy - 5:cy + 5, cx - 5:cx + 5]

        # Calculate the average HSV color in the region
        average_hsv_color = np.mean(color_region, axis=(0, 1)).astype(int)
        print(average_hsv_color)

        # Classify the color based on the color_ranges
        color = self.classify_color(average_hsv_color)

        # Append the detected color's name to the list
        self.imgdata.color.append(color)

    def classify_color(self, hsv_color):
        # You can implement a color classification logic here based on the HSV color values.
        # For now, I'm assuming a simple classification based on hue value.
        hue = hsv_color[0]

        if 0 <= hue < 10:
            return 'red'
        elif 35 <= hue < 85:
            return 'green'
        elif 100 <= hue < 130:
            return 'blue'
        elif 20 <= hue < 30:
            return 'yellow'
        elif 130 <= hue < 160:
            return 'violet'
        else:
            return 'unknown'