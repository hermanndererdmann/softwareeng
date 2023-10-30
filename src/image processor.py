import cv2 
import numpy as np 

class ImgData:
    def __init__(self):
        self.img = None
        self.pattern = []
        self.color = []
        self.contour = []



class image_processor:
    def __init__(self):
        self.imgdata=ImgData()
 
    def detect_shapes(self, img):

        # Create lists to store the detected patterns with their shapes and contours
        detected_patterns = []
        pattern_shapes = []
        pattern_contours = []

        # setting threshold of gray image 
        self.gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # Apply Gaussian blur to reduce noise
        self.blurred = cv2.GaussianBlur(self.gray, (5, 5), 0)

        # Detect edges using Canny edge detection
        self.edges = cv2.Canny(self.blurred, 50, 150)

        # Find contours in the edge image
        contours, _ = cv2.findContours(self.edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        for contour in contours[1:]:
            # Approximate the shape
            epsilon = 0.04 * cv2.arcLength(contour, True)
            approx = cv2.approxPolyDP(contour, epsilon, True)

            # Determine the shape based on the number of vertices
            num_vertices = len(approx)

            # Get the center of the shape
            M = cv2.moments(contour)
            if M['m00'] != 0:
                cx = int(M['m10'] / M['m00'])
                cy = int(M['m01'] / M['m00'])

                # Store the detected pattern information
                detected_patterns.append((cx, cy))
                pattern_shapes.append(num_vertices)
                pattern_contours.append(contour)

        return detected_patterns, pattern_shapes, pattern_contours

    def detect_colors(self):

        # Create lists to store the detected colors
        pattern_colors = []

        # Convert the image to the HSV color space
        self.hsv_img = cv2.cvtColor(self.img, cv2.COLOR_BGR2HSV)

        # Define color ranges for the specified colors
        color_ranges = {
            'red': [(0, 100, 100), (10, 255, 255)],
            'green': [(35, 100, 100), (85, 255, 255)],
            'blue': [(100, 100, 100), (130, 255, 255)],
            'yellow': [(20, 100, 100), (30, 255, 255)],
            'violet': [(130, 100, 100), (160, 255, 255)],
        }

        for color, (lower, upper) in color_ranges.items():
            # Create a mask for the specific color
            lower_color = np.array(lower, dtype=np.uint8)
            upper_color = np.array(upper, dtype=np.uint8)
            color_mask = cv2.inRange(self.hsv_img, lower_color, upper_color)

            # Find contours for the color regions
            contours, _ = cv2.findContours(color_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

            for contour in contours:
                pattern_colors.append(color)

        return pattern_colors

    def process_image(self):
        
        # Detect shapes
        detected_patterns, pattern_shapes, pattern_contours = self.detect_shapes()
        
        # Detect colors
        pattern_colors = self.detect_colors()

        # Set the processed image data to the imgdata object
        self.contour = pattern_contours
        self.imgdata.img = self.img
        self.imgdata.pattern = pattern_shapes
        self.imgdata.color = pattern_colors
        self.imgdata.contour = self.contour

        