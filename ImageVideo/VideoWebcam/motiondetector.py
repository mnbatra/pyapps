import cv2,time,pandas
from datetime import datetime
df=pandas.DataFrame(columns=["Start","End"])
df=
firstframe = None
status_list=[None,None]
ttime=[]

capture=cv2.VideoCapture(0)
time.sleep(2)
while True:
    check, frame = capture.read()
    status=0

    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    gray=cv2.GaussianBlur(gray,(21,21),0)


    if firstframe is None:
        firstframe = gray
        continue

    deltaframe=cv2.absdiff( firstframe, gray )
    threshf=cv2.threshold(deltaframe,30,255,cv2.THRESH_BINARY)[1]
    threshf=cv2.dilate(threshf, None, iterations=2)

    (_,cnts,_)=cv2.findContours(threshf.copy(),cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in cnts:
        if cv2.contourArea(contour)<10000:
            continue
        status=1
        (x,y,w,h)=cv2.boundingRect(contour)
        cv2.rectangle( frame, (x,y), (x+w,y+h), (0,255,0), 3 )

    status_list.append(status)

    if status_list[-1]==1 and status_list[-2]==0:
        ttime.append(datetime.now())
    if status_list[-1]==0 and status_list[-2]==1:
        ttime.append(datetime.now())
    status_list.append(status)

    status_list=status_list[-2:]

    cv2.imshow("threshold frame", threshf)
    cv2.imshow("Difference",deltaframe)
    cv2.imshow("Motion Detected",frame)
    #  time.sleep(3)
    key=cv2.waitKey(1)
    if key==ord('q'):
        if status==1:
            ttime.append(datetime.now())
        break

print(status_list)
print(ttime)

for i in range(0,len(ttime),2):
    df=df.append({"Start":ttime[i],"End":ttime[i+1]},ignore_index=True)
    df.to_csv("ActivityLog.csv")


capture.release()

cv2.destroyAllWindows
