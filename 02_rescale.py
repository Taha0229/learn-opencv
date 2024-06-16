import cv2 as cv

capture = cv.VideoCapture("videos/dog.mp4")

def rescale(frame, scale=0.75):
    # Works for Images, Videos and Live streams
    height = int(frame.shape[0] * scale)
    width = int(frame.shape[1] * scale)
    
    dimension = (width, height)
    
    return cv.resize(frame, dimension, interpolation=cv.INTER_AREA)
    # when scaling down use interpolation = cv.INTER_AREA when scaling up use interpolation = cv.cubic(slow) / cv.linear

def changeRes(width, height):
    # Works only for live streams
    # there are more values other than 3 and 4 for tuning the video
    capture.set(3, width)
    capture.set(4, height)
    

while True:
    isReadSuccess, frame = capture.read()
    
    cv.imshow("Original Video", frame)
    cv.imshow("Resized Video", rescale(frame, scale=0.2))
    
    if cv.waitKey(20) & 0xFF == ord('w'):
        break
    
capture.release()   
cv.destroyAllWindows()
        
    