import numpy as np

CAMERA_INDEX = 0

LOWER_COLOR = np.array([35, 70, 70])
UPPER_COLOR = np.array([85, 255, 255])

MIN_AREA = 30

# x,y,w,h
DRUMS = {
    "snare": (100, 300, 150, 150),
    "kick":  (300, 300, 150, 150),
    "hihat": (500, 300, 150, 150)
}

HIT_DELAY = 0.2 

MAX_SPEED = 1000 
