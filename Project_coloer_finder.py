import cv2
import numpy as np

frameWidth = 640
frameHeight = 480
cap = cv2.VideoCapture(0)  # 0 to cam default
cap.set(3, frameWidth)
cap.set(4, frameHeight)
cap.set(10, 150)

myColor = []


def findColor(img):
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    # lower = np.array([h_min, s_min, v_min])
    # upper = np.array([h_max, s_max, v_max])
    # mask = cv2.inRange(imgHSV, lower, upper)
    # cv2.imshow("img", mask)


while True:
    success, img = cap.read()
    cv2.imshow("Cam", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
