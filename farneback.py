import math

import numpy as np
import cv2
# flow	=	cv.calcOpticalFlowFarneback(	prev, next, flow, pyr_scale, levels, winsize, iterations, poly_n, poly_sigma, flags	)

def FarnebackPrepareGaussian(n, sigma, g, xg, xxg, ig11, ig03, ig33, ig55):
    if(sigma < 1.192092896E-07):
        sigma = n*0.3

    s = 0.0
    for x in range(-n, n+1):
        g[x] = math.exp(-x*x / (2*sigma*sigma))
        s += g[x]

    s = 1.0/s
    for x in range(-n, n+1):
        g[x] = g[x]*s
        xg[x] = x*g[x]
        xxg[x] = x*x*g[x]

    G = np.zeros(6, 6)
    for y in range(-n, n+1):
        for x in range(-n, n+1):
            G[0][0] += g[y]*g[x]
            G[1][1] += g[y]*g[x]*x*x
            G[3][3] += g[y]*g[x]*x*x*x*x
            G[5][5] += g[y]*g[x]*x*x*y*y
    G[2][2] = G[0][3] = G[0][4] = G[3][0] = G[4][0] = G[1][1]
    G[4][4] = G[3][3]
    G[3][4] = G[4][3] = G[5][5]

    invG = np.linalg.inv(G)
    ig11 = invG[1][1]
    ig03 = invG[0][3]
    ig33 = invG[3][3]
    ig55 = invG[5][5]

def FarnebackPolyExp(image, n, sigma):
    width = image.shape[0]
    height = image.shape[1]

    return image

def FarnebackUpdateMatrices():


def FarnebackUpdateFlow_Blur():

def preProcess(image):
    image = cv2.GaussianBlur(image)
    image = cv2.resize(image, cv2.INTER_LINEAR)
    image = FarnebackPolyExp()

for k in range(levels):
    if prvsFlow.size == 0:
        flow = np.zeros(height, width)
    else:
        flow = cv2.resize(prvsFlow, (width, height), cv2.INTER_LINEAR)
        flow *= 1.0/pyrScale_
    prvs = preProcess(prvs)
    curr = preProcess(curr)
    FarnebackUpdateMatrices(prvs, curr)

    for i in range(iterations):
        FarnebackUpdateFlow_Blur()

    prvsFlow = flow
