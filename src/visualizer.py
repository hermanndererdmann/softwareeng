import cv2 

class visualizer:
    def __init__(self) -> None:
        pass

    def get_imgdata(self, imgdata): 
        self.img = imgdata.img
        self.pattern = imgdata.pattern
        self.color = imgdata.color
        self.contour = imgdata.contour
        self.__draw_overlay()

    def show_overlay(self):
        #show overlay
        cv2.imshow('Overlay', self.img)

        
    def __draw_overlay(self):
        i = 0
        for contour in self.contour: 
            # cv2.approxPolyDP() function to approximate the shape 
            approx = cv2.approxPolyDP( 
                contour, 0.01 * cv2.arcLength(contour, True), True) 
                
            # using drawContours() function 
            cv2.drawContours(self.img, [contour], 0, (0, 0, 255), 5) 
            
            # finding the center point of the shape 
            M = cv2.moments(contour) 
            if M['m00'] != 0.0: 
                x = int(M['m10'] / M['m00']) 
                y = int(M['m01'] / M['m00']) 

            #add text to the overlay
            texttoprint = self.color[i] + "," + self.pattern[i]
            cv2.putText(self.img, texttoprint, (x, y), 
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)

            i += 1

