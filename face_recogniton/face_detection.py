import cv2 as cv
import os

img = cv.imread("../images/lady.jpg")


gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Gray scale image", gray)

haar_cascade = cv.CascadeClassifier("haar_face.xml")
faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=3)

print(f"Number of faces detected {len(faces_rect)}")

for (x,y,w,h) in faces_rect:
    cv.rectangle(img, (x,y), (x+w, y+h), (0,256,0), thickness=3)

cv.imshow("Lady", img)
print(f"face_rect: {faces_rect}")

cv.waitKey(0)