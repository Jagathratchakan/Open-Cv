import cv2 as cv
import mediapipe as mp


class Fashmesh():

    def __init__(self):
        self.mpDraw = mp.solutions.drawing_utils
        self.mpFashmesh = mp.solutions.face_mesh
        self.fashmesh = self.mpFashmesh.FaceMesh()

    def findface(self, frame, draw=True):
        img = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
        self.results = self.fashmesh.process(img)

        if self.results.multi_face_landmarks:
            for facelms in self.results.multi_face_landmarks:
                self.mpDraw.draw_landmarks(frame, facelms , self.mpFashmesh.FACEMESH_CONNECTION)

        return frame



def main():
    video = cv.VideoCapture(0)
    faceMesh = Fashmesh()
    while True:
        _, frame = video.read()
        frame = faceMesh.findface(frame)
        cv.imshow("Test", frame)
        k = cv.waitKey(1)
        if k == ord("q"):
            break

    video.release()
    cv.destroyAllWindows()

if __name__ == "__main__":
    main()