import math

import numpy as np
import cv2

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

def FarnebackPolyExp(src, n, sigma):
    width = int(round(src.shape[1]))
    height = int(round(src.shape[0]))
    kbuf = np.zeros(n*6 + 3, dtype=np.float)
    _row = np.zeros((width + n*2)*3, dtype=np.float)
    g = kbuf + n;
    xg = g + n*2 + 1;
    xxg = xg + n*2 + 1;
    row = _row + n*3;
    ig11 = 0.0
    ig03 = 0.0
    ig33 = 0.0
    ig55 = 0.0

    FarnebackPrepareGaussian(n, sigma, g, xg, xxg, ig11, ig03, ig33, ig55)

    dst = np.empty((height, width, 5))

    for y in range(height):
       for x in range(width):
           pass
       for k in range(1, n+1):
           pass

       for x in range(n*3):
           pass
       for x in range(width):
           pass

    row -= n*3

    return dst

def FarnebackUpdateMatrices():


def FarnebackUpdateFlow_Blur(frame0, frame1, flow, interM, block_size, update_matrices):
    width = flow.shape[1]
    height = flow.shape[0]
    m = block_size/2
    y0 = 0
    min_update_stripe = max(1<<10/width, block_size)
    scale = 1.0/block_size*block_size



    return flow


def calcOpticalFlowFarneback(prvs, curr, ioflow, pyr_scale, numLevels, winsize, iterations, poly_n, poly_sigma, flags):
    min_size = 32
    outFlow = np.empty([prvs.shape[0], prvs.shape[1], 2])
    prvsFlow = None
    levels = numLevels

    pyramidLevel = 0
    scale = 1.0
    for k in range(levels):
        scale *= pyr_scale
        if(prvs.shape[1]*scale < min_size || prvs.shape[0]*scale < min_size)
        pyramidLevel += 1

    for k in range(pyramidLevel, -1, -1):
        scale = 1.0
        for i in range(k):
            scale *= pyr_scale
        sigma = (1.0/scale - 1)*0.5
        smooth_sz = max( int(round(sigma*5)) | 1, 3 )
        width = int(round(prvs.shape[1]*scale))
        height = int(round(prvs.shape[0]*scale))

        if(k>0):
            flow = np.empty((height, width, 2))
        else:
            flow = outFlow
        if(prvsFlow == None):
            flow = np.zeros((height, width, 2))
        else:
            flow = cv2.resize(prvsFlow, (width, height), 0, 0, cv2.INTER_LINEAR)
            flow *= 1./pyr_scale

        prvs = cv2.GaussianBlur(prvs, (smooth_sz, smooth_sz), sigma, sigma)
        prvs = cv2.resize(prvs, (width, height), cv2.INTER_LINEAR)
        prvs = FarnebackPolyExp(prvs, poly_n, poly_sigma)

        FarnebackUpdateMatrices(prvs, curr)

        for i in range(iterations):
            FarnebackUpdateFlow_Blur(prvs, curr)

        prvsFlow = flow

    return outFlow
