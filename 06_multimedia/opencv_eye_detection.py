import cv2

# get xml filter/classifier
face_cascade = cv2.CascadeClassifier('./xml/face.xml')
eye_cascade = cv2.CascadeClassifier('./xml/eye.xml')

# get image
img = cv2.imread('./pictures/Avengers.jpg')
# convert to gray scale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# detect face on the image
# return coordinate
faces = face_cascade.detectMultiScale(gray)

# show detected faces
for (x, y, w, h) in faces:
    #         overlay, start,  finish,     BGR,    weight
    cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
    
    # ROI(Region of Interest, 관심영역)
    roi_color = img[y:y+h, x:x+w]
    roi_gray = gray[y:y+h, x:x+w]

    # detect eyes
    eyes = eye_cascade.detectMultiScale(roi_gray)

    for (ex, ey, ew, eh) in eyes:
        cv2.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (0, 255, 0), 2)

cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()