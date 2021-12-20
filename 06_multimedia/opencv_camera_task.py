# opencv_camera_task.py
import cv2

cam = cv2.VideoCapture(0)

if not cam.isOpened():
    print('Opening camera failed')
    exit(0)

while True:
    ret, frame = cam.read()
    if not ret:
        break

    edge = cv2.Canny(frame, 120, 70)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow('default', frame)
    cv2.imshow('edge', edge)
    cv2.imshow('gray', gray)

    if cv2.waitKey(10) == 13:
        break

cam.release()
cv2.destroyAllWindows()