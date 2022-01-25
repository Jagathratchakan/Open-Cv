import cv2 as cv
import os
import mediapipe as mp
import HandTracking as ht
import math
import numpy as np


FolderPath = "img"
myList = os.listdir(FolderPath)
overlayout = []


for impath in myList:
    image = cv.imread(f'{FolderPath}/{impath}')
    overlayout.append(image)

header = overlayout[3]

video = cv.VideoCapture(0)
detector = ht.handDetect()

xp , yp = 0,0
imgCanvas = np.zeros((720,1200, 3),np.uint8)


tipIds = [4,8,12,16,20]
def make_720():
    video.set(3,1080)
    video.set(4,720)


while True:
    _,frame=video.read()
    #frame[170:1080, 0:400] = header
    frame = detector.findhand(frame)
    lmlist = detector.findpostion(frame,draw=False)

    if len(lmlist) != 0:
        x1,y1 = lmlist[8][1:]
        x2, y2 = lmlist[12][1:]
        fingures = detector.fingureup()
        #print(fingures)
        #Erase mode
        if fingures[1] and fingures[2] == False:
            cv.circle(frame, (x1, y1), 10, (0, 50, 210), cv.FILLED)
            if xp == 0 and yp == 0:
                xp, yp = x1, y1
            cv.line(frame, (xp, yp), (x1, y1), (130, 50, 120), 15)
            cv.line(imgCanvas, (xp, yp), (x1, y1), (130, 50, 120), 10)
            xp, yp = x1, y1
        elif fingures[1] and fingures[2]:
            cv.line(frame, (xp, yp), (x1, y1), (0, 0, 0), 15)
            cv.line(imgCanvas, (xp, yp), (x1, y1), (0, 0, 0), 40)

        else:
            pass

    cv.imshow("Test", frame)
    cv.imshow("cam",imgCanvas)
    k = cv.waitKey(1)
    if k == ord("q"):
        break

video.release()
cv.destroyAllWindows()