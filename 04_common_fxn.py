import cv2 as cv

img = cv.imread("images/park.jpg")
cv.imshow("Original Image", img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Grayscale Image", gray)

gaussian_blur = cv.GaussianBlur(img, (3,3), cv.BORDER_DEFAULT)
cv.imshow("Blur Image", gaussian_blur)

canny_edge = cv.Canny(img, 150, 200)
cv.imshow("Edge detection using Canny1", canny_edge)
# canny_edge = cv.Canny(img, 10, 25)
# cv.imshow("Edge detection using Canny2", canny_edge)
# canny_edge = cv.Canny(img, 175, 200)
# cv.imshow("Edge detection using Canny3", canny_edge)

# add pixels to the object boundaries
dilate = cv.dilate(canny_edge, (7,7), iterations=3)
cv.imshow("Dilated", img)

# removes pixels from the object boudaries
erode = cv.erode(dilate, (7,7), iterations=3)
cv.imshow("Eroded", erode)

cropped = img[0:250,:]
cv.imshow("Cropped", cropped)
cv.waitKey(0)