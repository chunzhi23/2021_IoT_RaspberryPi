import cv2

# 이미지 파일 읽어오기
img = cv2.imread('./pictures/kim_gu.jpg')
# 이미지 크기 바꾸기
img2 = cv2.resize(img, (512, 768))

# Edge선 추출하기
edge1 = cv2.Canny(img, 50, 100)
edge2 = cv2.Canny(img, 100, 150)
edge3 = cv2.Canny(img, 150, 200)

# 이미지를 'kim_gu'라는 이름의 창으로 띄우기
cv2.imshow('KimGu', img2)
cv2.imshow('Edge1', edge1)
cv2.imshow('Edge2', edge2)
cv2.imshow('Edge3', edge3)

# 아무 키를 누르기까지 기다리기
cv2.waitKey(0)

# 대기가 끝난 후 연 모든 창을 닫기
cv2.destroyAllWindows()