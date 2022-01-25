import cv2 as cv
import os
import mediapipe as mp
import HandTracking as ht
import math



video = cv.VideoCapture(0)
detector = ht.handDetect()

tipIds = [4,8,12,16,20]

while True:
    _,frame=video.read()

    frame = detector.findhand(frame)
    lmlist = detector.findpostion(frame,draw=False)

    if len(lmlist) != 0:
        fingures = []

        if lmlist[tipIds[0]][1] > lmlist[tipIds[0] - 1][1]:
            fingures.append(1)
        else:
            fingures.append(0)

        for id in range(1,5):
            if lmlist[tipIds[id]][2] < lmlist[tipIds[id]-2][2]:
                fingures.append(1)
            else:
                fingures.append(0)

        if fingures[0] == 1:
            print("Thump Fingure")
        elif fingures[1] == 1:
            print("Index Fingure")
        elif fingures[2] == 1:
            print("Middle Fingure")
        elif fingures[3] == 1:
            print("Ring Finger")
        elif fingures[4] == 1:
            print("Pink Fingure")
        else:
            print("Unknown")

    cv.imshow("Test", frame)
    k = cv.waitKey(1)
    if k == ord("q"):
        break

video.release()
cv.destroyAllWindows()