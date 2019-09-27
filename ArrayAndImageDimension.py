import os
import cv2
import numpy as np

print("exiv2:")
os.system("exiv2 lenna_full.jpg")

img = cv2.imread("lenna_full.jpg")
print("numpy array [0]: {}".format(img.shape[0]))
print("numpy array [1]: {}".format(img.shape[1]))

cv2.imshow("lenna_full.jpg", img)
cv2.waitKey(0)

cv2.imwrite("lenna_full_duplicate.jpg", img)
print("exiv2:")
os.system("exiv2 lenna_full_duplicate.jpg")

cv2.destroyAllWindows()
