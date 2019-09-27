import cv2
import numpy as np

img = cv2.imread("lenna_full.jpg")

center = (img.shape[1]//2, img.shape[0]//2)
img = cv2.drawMarker(img, center, color=(255, 0, 255))

cv2.imshow("lenna_full.jpg", img)
cv2.waitKey(0)

cv2.destroyAllWindows()
