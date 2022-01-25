import cv2 as cv
import mediapipe as mp


class position():
    def __init__(self):
        self.mpface = mp.solutions.face_detection
        self.face = self.mpface.FaceDetection(0.75)
        self.myDraw = mp.solutions.drawing_utils

    def findface(self,frame,draw=True):
        imgRBG = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
        self.results = self.face.process(imgRBG)

        if self.results.detections:
            for id , detection in enumerate(self.results.detections):
                box = detection.location_data.relative_bounding_box
                h,w,c = frame.shape

                bbox = int(box.xmin*w) , int(box.ymin*h), int(box.width*w),int(box.height*h)

                cv.rectangle(frame,bbox,(255,0,255),2)
        return frame




def main():
    cap = cv.VideoCapture(0)
    position_obj = position()
    while True:
        _, frame = cap.read()
        frame = position_obj.findface(frame)
        cv.imshow("Test", frame)
        k = cv.waitKey(1)
        if k == ord("q"):
            break

    cap.release()
    cv.destroyAllWindows()


if __name__ == "__main__":
    main()