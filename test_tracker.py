import cv2
from tracker import StickTracker
from config import CAMERA_INDEX

cap = cv2.VideoCapture(CAMERA_INDEX)

if not cap.isOpened():
    print("Camera could not be opened")
    exit()


tracker = StickTracker()

while True:
    ret,frame = cap.read()

    if not ret or frame is None:
        print("Failed to grab frame from camera")

    frame = cv2.flip(frame,1)

    position,speed,mask = tracker.detect(frame)

    cv2.putText(frame,f"Speed: {speed:.2f}",(10,30),
                    cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2)

    if position:
        cx,cy = position
        cv2.circle(frame,(cx,cy),10,(0,0,255),-1)
        cv2.putText(frame, f"({cx},{cy})", (cx+10, cy),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,255), 2)
        
    cv2.imshow("Stick Tracker",frame)
    cv2.imshow("Mask",mask)

    if cv2.waitKey(1) & 0xFF == 27:
        break
    
cap.release()
cv2.destroyAllWindows()
