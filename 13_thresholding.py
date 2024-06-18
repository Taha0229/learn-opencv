import cv2 as cv
import numpy as np

img = cv.imread("images/cats.jpg")
cv.imshow("Cats image", img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Gray image", gray)

# 1. Simple Threshold
thresholdValue, thresholdImage = cv.threshold(gray, 150, 255, cv.THRESH_BINARY)
cv.imshow("Simple Threshold", thresholdImage)

# 2. Simple Threshold Inverse
thresholdValueInv, thresholdImageInv = cv.threshold(gray, 150, 255, cv.THRESH_BINARY_INV)
cv.imshow("Simple Threshold Inverse", thresholdImageInv)

# 3. Adaptive Threshold

adaptive_threshold = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 3)
cv.imshow("Adaptive Threshold", adaptive_threshold)

cv.waitKey(0)