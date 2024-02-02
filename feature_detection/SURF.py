"""
SURF: Speeded Up Robust Features
SIFTと比較して、高速な検出器・記述子
マッチングの精度を保ちつつ、3倍の高速化を実現

"""

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('img/thorino.jpg', 0)
surf = cv2.SURF(400)
surf.hessianThreshold = 50000
kp, des = surf.detectAndCompute(img,None)

img2 = cv2.drawKeypoints(img,kp,None,(255,0,0),4)
plt.imshow(img2)
plt.show()