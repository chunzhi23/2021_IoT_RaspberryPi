import cv2

img = cv2.imread('./pictures/kim_gu.jpg')

# 그레이 스케일로 변환하기
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imshow('Papago', img)
cv2.imshow('Papago_gray', img_gray)

# ASCII = American Standard Code for Information Interchange
while True:
    # 엔터가 입력될 때까지 기다리기
    if cv2.waitKey(0) == 13:
        break

# 파일로 저장하기
cv2.imwrite('./pictures/papago_gray.png', img_gray)

cv2.destroyAllWindows()