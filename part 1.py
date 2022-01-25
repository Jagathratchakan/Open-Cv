import cv2 as cv
import numpy as np
import os

#img = cv.imread("C:/Users/Sanjay/Downloads/t.jpg")
#cv.imshow("Test",img)

haar_cascade = cv.CascadeClassifier('haar_face.xml')
# Contour Detection
def gray():
    gray_1 = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    cv.imshow("test1",gray_1)

def canny():
    can = cv.Canny(img,150,200)
    cv.imshow("test2",can)
###################################################################################################################
# DETECT THE HUMAN FACES BY USING CV2 AND HAAR CASACADE DATASET FOR FACIAL MARKS
def face():
    haar_cascade = cv.CascadeClassifier('haar_face.xml')

    face_rect = haar_cascade.detectMultiScale(img,scaleFactor=1.1,minNeighbors=6)
    for (x,y,w,h) in face_rect:
        cv.rectangle(img,(x,y),(x+w,y+h), (0,255,0) , thickness=2)

    cv.imshow("Detected",img)
##################################################################################################################

def identify():
    people = ["Barack Obama","Donald Trump"]
    Dir = r"E:\img"
    global features
    features = []
    labels = []

    for person in people:
        path =  os.path.join(Dir,person)
        label = people.index(person)

        for img in os.listdir(path):
            img_path = os.path.join(path,img)

            img_arr = cv.imread(img_path)
            gray = cv.cvtColorTwoPlane(img_arr,cv.COLOR_BGR2GRAY)

            face_rect = haar_cascade.detectMultiScale(img, scaleFactor=1.1, minNeighbors=3)
            for (x, y, w, h) in face_rect:
                faces_rol = gray[y:y+h,x:x+w]
                features.append(faces_rol)
                labels.append(label)


identify()
print(f'Length of the features = {len(features)}')
cv.waitKey(0)
