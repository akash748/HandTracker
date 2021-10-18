import cv2
import mediapipe as mp
import time


class handDetetctor():
    def __init__(self,mode= False,maxHands = 2,detectionCon = 0.5,trackCon = 0.5):
        self.mode = mode
        self.maxHands = maxHands
        self.detectionCon = detectionCon
        self.trackCon = trackCon
        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(self.mode,self.maxHands,self.detectionCon,self.trackCon)
        self.mpDraw = mp.solutions.drawing_utils

    def findHands(self):
        imgRGB = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        results = self.hands.process(imgRGB)
        if results.multi_hand_landmarks:
            for i in results.multi_hand_landmarks:
                for id,lm in enumerate(i.landmark):
                    h,w,c = img.shape
                    cx,cy = int(lm.x*w), int(lm.y*h)
                    #print(id,cx,cy)
                self.mpDraw.draw_landmarks(img,i,self.mpHands.HAND_CONNECTIONS)

        current_time = time.time()
        fps = 1/(current_time-previous_time)
        previous_time = current_time

        cv2.putText(img,str(int(fps)),(10,70),cv2.FONT_HERSHEY_PLAIN,3,(0,255,255),4)




def main():
    current_time = 0
    previous_time = 0
    cap = cv2.VideoCapture(0)

    while True:
        success, img = cap.read()

        current_time = time.time()
        fps = 1 / (current_time - previous_time)
        previous_time = current_time

        cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3, (0, 255, 255), 4)

        cv2.imshow("Image", img)
        cv2.waitKey(1)






if __name__ == "__main__":
    main()