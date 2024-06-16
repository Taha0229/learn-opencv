import cv2 as cv

# Read video

capture = cv.VideoCapture("videos/dog.mp4")

while True:
    # the VideoCapture returns two values, boolean -> T if read operation is success 
    # numpy array -> The actual frame
    
    isReadSuccess,frame = capture.read()  
    
    # Since the frame is an numpy array, need to use imshow to process it
    
    cv.imshow("Video", frame)
    
    # & must be used 'and' won't work
    if cv.waitKey(20) & 0xFF==ord('w'):
        break
    
# Release the capture device    

capture.release()

# Exit gracefully

cv.destroyAllWindows()