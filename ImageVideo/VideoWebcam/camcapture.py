import cv2
import time

capture=cv2.VideoCapture(0)

a=0

while True:

    check, frame =capture.read()
    print(check)
    print(frame)
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.imshow("Capturing",gray)
    #  time.sleep(3)
    key=cv2.waitKey(1)
    if key==ord('q'):
        break

    a=a+1
print(a)
capture.release()

cv2.destroyAllWindows
