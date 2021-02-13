import cv2

# ____ read image file ____
img = cv2.imread("")
cv2.imshow("Output", img)
cv2.waitKey(0)

# ____ read video file ____
cap = cv2.VideoCapture("")
while True:
    success, img = cap.read()
    cv2.imshow("Video", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# ____ read cam ____
cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)
cap.set(10, 100)
while True:
    success, img = cap.read()
    cv2.imshow("Cam", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
