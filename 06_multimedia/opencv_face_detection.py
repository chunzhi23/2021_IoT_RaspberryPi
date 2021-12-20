import cv2

# get xml filter/classifier
face_cascade = cv2.CascadeClassifier('./xml/face.xml')

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

cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()