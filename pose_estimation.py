import cv2 as cv
import mediapipe as mp

"""cap = cv.VideoCapture(0)

mpPose = mp.solutions.pose
pose = mpPose.Pose()
myDraw = mp.solutions.drawing_utils
while True:
    _,frame=cap.read()
    imgRBG = cv.cvtColor(frame,cv.COLOR_BGR2RGB)
    results = pose.process(imgRBG)

    if results.pose_landmarks:
        myDraw.draw_landmarks(frame,results.pose_landmarks,mpPose.POSE_CONNECTIONS)

    cv.imshow("Test", frame)
    k = cv.waitKey(1)
    if k == ord("q"):
        break

cap.release()
cv.destroyAllWindows()"""
class position():
    def __init__(self):
        self.mpPose = mp.solutions.pose
        self.pose = self.mpPose.Pose()
        self.myDraw = mp.solutions.drawing_utils

    def findBody(self,frame,draw=True):
        imgRBG = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
        self.results = self.pose.process(imgRBG)

        if self.results.pose_landmarks:
            self.myDraw.draw_landmarks(frame, self.results.pose_landmarks, self.mpPose.POSE_CONNECTIONS)
        return frame

    def findpostion(self,frame,handNo=0,draw= True):

        lmlist = []

        if self.results.pose_landmarks:
            for id , ln in enumerate(self.results.pose_landmarks.landmark):
                h,w,c = frame.shape
                cx,cy =int(ln.x*w), int(ln.y*h)
                lmlist.append([id,cx,cy])
                if draw:
                    cv.circle(frame,(cx,cy),5,(255,0,255),cv.FILLED)
        return lmlist

def main():
    cap = cv.VideoCapture(0)
    position_obj = position()

    while True:
        _, frame = cap.read()
        frame = position_obj.findBody(frame)
        lmlist = position_obj.findpostion(frame,draw=False)
        if len(lmlist) !=0:
            print(lmlist[14])
            cv.circle(frame,(lmlist[14][1],lmlist[14][2]), 15, (0, 0, 255), cv.FILLED)
        cv.imshow("Test", frame)
        k = cv.waitKey(1)
        if k == ord("q"):
            break

    cap.release()
    cv.destroyAllWindows()


if __name__ == "__main__":
    main()
