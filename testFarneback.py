from numpy.testing import assert_array_equal
import cv2

import farneback

path = "assets/Wooden/"

prvs = cv2.imread(path + "frame10.png", cv2.IMREAD_GRAYSCALE)
curr = cv2.imread(path + "frame11.png", cv2.IMREAD_GRAYSCALE)

flow = cv2.calcOpticalFlowFarneback(prvs, curr, None, 0.5, 3, 15, 3, 5, 1.2, 0)
scratchFlow = farneback.calcOpticalFlowFarneback(prvs, curr, None, 0.5, 3, 15, 3, 5, 1.2, 0)

assert_array_equal(flow, scratchFlow)
