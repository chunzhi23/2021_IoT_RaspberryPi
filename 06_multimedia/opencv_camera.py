import cv2, time

# 카메라 사용
cam = cv2.VideoCapture(0)
now_str = time.strftime('%Y%m%d_%H%M%S')

# 카메라가 사용가능한지 확인
if not cam.isOpened():
    print('Camera open failed')
    exit()

# 사진 촬영
# ret, frame = cam.read()

# cv2.imshow('photo_%s' % now_str, frame)
# cv2.imwrite('./pictures/photo_%s.jpg' % now_str, frame)

# while cv2.waitKey(0) == 13:
#     break

# 동영상 촬영
while True:
    ret, frame = cam.read()
    if not ret:
        break

    cv2.imshow('frame', frame)
    if cv2.waitKey(10) == 13:
        break

# 카메라 사용 종료
cam.release()
cv2.destroyAllWindows()