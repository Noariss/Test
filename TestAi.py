import cv2
import numpy as np
import time
import PoseModule as pm

cap = cv2.VideoCapture("F:/tryingAI/Squat.mp4")
count = -0.5
dir = 0
detector = pm.poseDetector()

while True:
    success, img = cap.read()
    #img = cv2.imread("F:/tryingAI/squat.jpg")
    #img = cv2.resize(img, (1280, 720))
    img = detector.findPose(img)
    lmList = detector.findPosition(img, False)
    if len(lmList) != 0:
        angle = detector.findAngle(img, 23, 25, 27)
        per = np.interp(angle,(90, 170), (0,100))

        if per == 100:
            if dir == 0:
                count += 0.5
                dir = 1
        if per == 0:
            if dir == 1:
                count += 0.5
                dir = 0

        cv2.putText(img, str(int(count)), (50,100), cv2.FONT_HERSHEY_PLAIN, 5, (255, 0, 0), 5)

    cv2.imshow("Image", img)
    cv2.waitKey(1)
