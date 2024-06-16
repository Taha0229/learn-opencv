import cv2 as cv

# Read image

img = cv.imread("images/cat.jpg")

# imshow() takes two arguments 1. Name of the window, 2. Actual image

# cv.imshow("Image", img)
cv.imshow("Image1", img[:,:,0])
cv.imshow("Image2", img[:,:,1])
cv.imshow("Image3", img[:,:,2])

# if wait key is not defined then the window will be destroyed immediately
# 0 -> wait infinitely until a key is pressed, integer -> wait for integer milliseconds 

cv.waitKey(0) 

