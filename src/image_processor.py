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

class processor:
    def __init__(self):
        self.imgdata = ImgData()


    def detect_shapes(self, img):
        self.imgdata.img = img
        pattern = []
        self.imgdata.color = []
        self.imgdata.contour = []
        cx = []
        cy = []
        # setting threshold of gray image 
        gray = cv2.cvtColor(self.imgdata.img, cv2.COLOR_BGR2GRAY)

        # Apply Gaussian blur to reduce noise
        blurred = cv2.GaussianBlur(gray, (5, 5), 0)

        # Detect edges using Canny edge detection
        edges = cv2.Canny(blurred, 50, 150)

        # Find contours in the edge image
        contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        for contour in contours:

            # filter for the right size
            if cv2.contourArea(contour) < 40 * 40:
               continue
            elif cv2.contourArea(contour) > 400 * 400:
                continue

            # Approximate the shape
            epsilon = 0.04 * cv2.arcLength(contour, True)
            approx = cv2.approxPolyDP(contour, epsilon, True)

            # Determine the shape based on the number of vertices
            num_vertices = len(approx)
            if num_vertices == 3:
                pattern.append("Triangle")
            elif num_vertices == 4:
                # Check the aspect ratio to determine Rectangle or Square
                x, y, w, h = cv2.boundingRect(contour)
                aspect_ratio = float(w) / h
                if 0.95 <= aspect_ratio <= 1.05:
                    pattern.append("Square")
                else:
                    pattern.append("Rectangle")
            elif 5 <= num_vertices <= 8:
                pattern.append("Circle")
            else:
                pattern.append("Unknown")

            # Calculate the centroid of the contour
            M = cv2.moments(contour)
            if M['m00'] != 0.0: 
                __cx = int(M['m10'] / M['m00'])
                __cy = int(M['m01'] / M['m00'])
            # Store the detected contour information
                cx.append(__cx)
                cy.append(__cy)
                self.imgdata.contour.append(contour)
                # Call detect_colors to detect color around the centroid
                self.__detect_colors(__cx, __cy)
        self.imgdata.cx = cx
        self.imgdata.cy = cy
        self.imgdata.pattern = pattern
        

        print(self.imgdata.color)


    def __detect_colors(self,  cx, cy):
        # Convert the image to the HSV color space
        hsv_img = cv2.cvtColor(self.imgdata.img, cv2.COLOR_BGR2HSV)

        # Extract color from a 5x5 region around the centroid (cx, cy)
        color_region = hsv_img[cy - 5:cy + 5, cx - 5:cx + 5]

        # Calculate the average HSV color in the region
        average_hsv_color = np.mean(color_region, axis=(0, 1)).astype(int)

        # Classify the color based on the color_ranges
        color = self.__classify_color(average_hsv_color)

        # Append the detected color's name to the list
        self.imgdata.color.append(color)

    def __classify_color(self, hsv_color):
        
        hue = hsv_color[0]

        if 0 <= hue < 10:
            return 'red'
        elif 10 <= hue < 30:
            return 'orange'
        elif 30 <= hue < 85:
            return 'yellow'
        elif 85 <= hue < 170:
            return 'green'
        elif 170 <= hue < 260:
            return 'blue'
        elif 260 <= hue < 320:
            return 'purple'
        elif 320 <= hue < 360:
            return 'red'  # Red wraps around, so consider it as a continuation of the red range.
        else:
            return 'unknown'