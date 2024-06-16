import cv2 as cv
import numpy as np

arr = np.zeros((500, 500, 3), dtype="uint8")

thickness = 3
if thickness == -1:
    thickness = arr.shape[0]
arr[arr.shape[0] // 2 : arr.shape[0] // 2 + thickness, :] = (255, 255, 255)
cv.circle(arr, (256,256), radius=260, thickness=-1, color=(256, 0, 0))
cv.ellipse(arr, (256,290), (230,240), 0, 0, 360, color=(0, 0, 0), thickness=6)
cv.ellipse(arr, (256,290), (230,240), 0, 0, 360, color=(255, 255, 255), thickness=-1)
cv.circle(arr, (255 - 3, 255 + 100), radius=100, thickness=3, color=(0, 0, 0))
cv.rectangle(
    arr,
    (250 - 100, 250+3),
    (250 + 104, 250 + 120),
    (255, 255, 255),
    thickness=-1,
)
# cv.rectangle(
#     arr,
#     (0 + thickness, 0 + thickness),
#     (250 - thickness, 250 - thickness),
#     (0, 250, 0),
#     thickness=-1,
# )

cv.circle(
    arr,
    (arr.shape[0] // 2 - 80, arr.shape[1] // 2 - 60),
    radius=80,
    thickness=3,
    color=(0, 0, 0),
)
cv.ellipse(arr,(arr.shape[0] // 2 - 80, arr.shape[1] // 2 - 60), (8,11),0, 0, 360, color=(0, 0, 0), thickness=-1)
cv.circle(
    arr,
    (arr.shape[0] // 2 - 80+2, arr.shape[1] // 2 - 60+6),
    radius=4,
    thickness=-1,
    color=(255,255,255),
)


cv.circle(
    arr,
    (arr.shape[0] // 2 + 80, arr.shape[1] // 2 - 60),
    radius=80,
    thickness=3,
    color=(0, 0, 0),
)
cv.ellipse(arr,(arr.shape[0] // 2 + 80, arr.shape[1] // 2 - 60), (8,11),0, 0, 360, color=(0, 0, 0), thickness=-1)
cv.circle(
    arr,
    (arr.shape[0] // 2 + 80+2, arr.shape[1] // 2 - 60+6),
    radius=4,
    thickness=-1,
    color=(255,255,255),
)

arr[250 : 250 + 120, 250 - (thickness) : 250 + (thickness)] = (0, 0, 0)
cv.circle(
    arr,
    (arr.shape[0] // 2, arr.shape[1] // 2),
    radius=20,
    thickness=-1,
    color=(0, 0, 256),
)
arr[250 + 120 : 250 + 120 + thickness, 250 - 99 : 250 + 103] = (0, 0, 0)
cv.line(arr, (250+25, 250+50), (250+140, 250+30), thickness=3, color=(0,0,0))
cv.line(arr, (250+25, 250+70), (250+140, 250+70), thickness=3, color=(0,0,0))
cv.line(arr, (250+25, 250+90), (250+140, 250+110), thickness=3, color=(0,0,0))

cv.line(arr, (250-25, 250+50), (250-140, 250+30), thickness=3, color=(0,0,0))
cv.line(arr, (250-25, 250+70), (250-140, 250+70), thickness=3, color=(0,0,0))
cv.line(arr, (250-25, 250+90), (250-140, 250+110), thickness=3, color=(0,0,0))
cv.rectangle(arr, (80,60), (420,120),(0,0,0), -1)
cv.putText(arr, "Cursed Doraemon", (100,100), cv.FONT_HERSHEY_TRIPLEX, 1, (0,256,0),2)

cv.imshow("Image", arr)
cv.waitKey(0)
