import cv2
import numpy as np
from config import LOWER_COLOR, UPPER_COLOR, MIN_AREA

class StickTracker:
    def __init__(self):
        self.prev_position=None

    def detect(self,frame):
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        mask = cv2.inRange(hsv,LOWER_COLOR,UPPER_COLOR)

        kernel = np.ones((5,5), np.uint8)
        mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
        mask = cv2.morphologyEx(mask, cv2.MORPH_DILATE, kernel)

        contours,_ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        if not contours:
            return None, mask
        
        largest = max(contours, key=cv2.contourArea)

        if cv2.contourArea(largest) < MIN_AREA:
            return None, mask
        
        x,y,w,h = cv2.boundingRect(largest)
        cx = x+w // 2
        cy = y+h // 2

        return (cx,cy), mask