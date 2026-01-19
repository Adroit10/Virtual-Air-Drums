import numpy as np

# Camera
CAMERA_INDEX = 0

# HSV color range for the stick tip (example: green)
# You will fine-tune these after testing
LOWER_COLOR = np.array([35, 70, 70])
UPPER_COLOR = np.array([85, 255, 255])

# Minimum contour area to be considered as stick
MIN_AREA = 30

# Drum Zones (x, y, width, height)
DRUMS = {
    "snare": (100, 300, 150, 150),
    "kick":  (300, 300, 150, 150),
    "hihat": (500, 300, 150, 150)
}

# Hit control
HIT_DELAY = 0.2  # seconds between two hits on same drum

# Speed to volume conversion
MAX_SPEED = 1000  # tune later
