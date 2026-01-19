import cv2
import numpy as np
import time
from config import DRUMS, HIT_DELAY, MAX_SPEED

class DrumController:

    def __init__(self,sound_player):
        self.sound_player = sound_player
        self.last_hit_time = {}

    def draw_drums(self,frame):

        for name, (x,y,w,h) in DRUMS.items():
            cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
            cv2.putText(frame,name.upper(),(x,y-10),cv2.FONT_HERSHEY_SIMPLEX,
                        0.6,(255,0,0),2)
            
    def check_hit(self,position,speed):

        if position is None:
            return
        
        cx,cy = position
        current_time = time.time()

        volume = min(speed/MAX_SPEED, 1.0)

        for drum_name, (x,y,w,h) in DRUMS.items():
            if x<cx<x+w and y<cy<y+h:
                last_time = self.last_hit_time.get(drum_name,0)

                if current_time - last_time > HIT_DELAY:
                    self.sound_player.play(drum_name,volume)
                    self.last_hit_time[drum_name] = current_time
                    

