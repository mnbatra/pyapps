import cv2

face_cascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

img=cv2.imread("news.jpg")
grayimg=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

faces=face_cascade.detectMultiScale(grayimg,
scaleFactor=1.1,
minNeighbors=5)


for x,y,w,h in faces:
    img=cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)

print(faces)

cv2.imshow("face", img)
cv2.waitKey(0)
cv2.destroyAllWindows()