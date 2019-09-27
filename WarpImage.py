import os
import cv2
import numpy as np

src = cv2.imread("lenna_full.jpg")

srcTri = np.array( [[0, 0], [src.shape[1]-1, 0], [0, src.shape[0]-1]] ).astype(np.float32)
dstTri = np.array( [[10, 10], [src.shape[1]+9, 10], [10, src.shape[0]+9]] ).astype(np.float32)
warp_mat = cv2.getAffineTransform(srcTri, dstTri)
warp_dst = cv2.warpAffine(src, warp_mat, (src.shape[1], src.shape[0]), borderValue=(0, 255, 255))

cv2.imwrite("lenna_full_shift10-10.jpg", warp_dst)
print("exiv2:")
os.system("exiv2 lenna_full_shift10-10.jpg")


srcQuad = np.array( [[0, 0], [src.shape[1]-1, 0], [src.shape[1]-1, src.shape[0]-1], [0, src.shape[0]-1]] ).astype(np.float32)
dstQuad = np.array( [[-100, -100], [src.shape[1]+99, -100], [src.shape[1]+99, src.shape[0]+99], [-100, src.shape[0]+99]] ).astype(np.float32)
warp_mat = cv2.getPerspectiveTransform(srcQuad, dstQuad)
warp_dst = cv2.warpPerspective(src, warp_mat, (src.shape[1], src.shape[0]), borderValue=(0, 255, 255))

cv2.imwrite("lenna_full_zoomin100-100.jpg", warp_dst)
print("exiv2:")
os.system("exiv2 lenna_full_zoomin100-100.jpg")

cv2.destroyAllWindows()
