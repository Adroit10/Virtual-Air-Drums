import cv2
import numpy as np
from config import LOWER_COLOR, UPPER_COLOR, MIN_AREA
import time

class StickTracker:
    def __init__(self):
        self.prev_position=None
        self.prev_time=None
        self.stable_frames=0

    def detect(self,frame):
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        mask = cv2.inRange(hsv,LOWER_COLOR,UPPER_COLOR)

        kernel = np.ones((3,3), np.uint8)
        mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
        mask = cv2.morphologyEx(mask, cv2.MORPH_DILATE, kernel)

        contours,_ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        if not contours:
            self.prev_position=None
            self.prev_time=None
            return None,0,mask
        
        largest = max(contours, key=cv2.contourArea)
        area = cv2.contourArea(largest)
        print("Contour Area:",area)

        if area < MIN_AREA:
            self.stable_frames=0
            return None,0,mask
        if area<120:
            self.stable_frames+=1
            if self.stable_frames<3:
                return None,0,mask
            else:
                self.stable_frames=0
                
        x,y,w,h = cv2.boundingRect(largest)
        cx = x+w // 2
        cy = y+h // 2

        current_time = time.time()
        speed = 0

        if self.prev_position and self.prev_time:
            dx = cx - self.prev_position[0]
            dy = cy - self.prev_position[1]
            dist = (dx**2 + dy**2)**0.5
            dt = current_time - self.prev_time
            if dt>0:
                speed = dist/dt

        self.prev_position = (cx,cy)
        self.prev_time = current_time

        return (cx,cy),speed, mask