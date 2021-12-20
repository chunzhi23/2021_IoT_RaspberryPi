import cv2, time

cam = cv2.VideoCapture(0)
now_str = time.strftime('%Y%m%d_%H%M%S')

if not cam.isOpened():
    print('Camera open failed')
    exit()

# fourcc, four character code: DIVX(avi), MP4V(mp4), X264(h264)
# *'DIVX' = 'D','I','V','X'
fourcc =  cv2.VideoWriter_fourcc(*'DIVX')

# 저장을 위한 세팅:    name                               fourcc, fps,frame size
out = cv2.VideoWriter('./videos/video_%s.avi' % now_str, fourcc, 30, (640, 480))

while True:
    ret, frame = cam.read()
    if not ret:
        break

    cv2.imshow('frame', frame)
    out.write(frame)
    if cv2.waitKey(10) == 13:
        break

cam.release()
out.release()
cv2.destroyAllWindows()