import cv2
import numpy as np

img = cv2.imread("car.jpg")
print(img.shape)

imgResize = cv2.resize(img, (600, 300))
print(imgResize.shape)

imgCropped = img[0:200, 200:500]

cv2.imshow("Image", img)
cv2.imshow("ImageResize", imgResize)
cv2.imshow("ImageCropped", imgCropped)
cv2.waitKey(0)
