import cv2
import numpy as np
"""
Canny法の理論
1. ガウシアンフィルタでノイズを除去する
2. Sobelフィルタで勾配を求める
3. 勾配の大きさと勾配の方向を求める  
4. 非極大値抑制→エッジの細線化(抑制する)
5. ヒステリシス閾値処理→○:maxval以上, ×:minval以下 繋がっていれば範囲の中でもエッジとする
"""
def nothing(x):
    pass

img = cv2.imread('img/imori.jpg', 0)

def canny(x):
    global img, minVal, maxVal
    minVal = cv2.getTrackbarPos('minVal','image')
    maxVal = cv2.getTrackbarPos('maxVal','image')
    edges = cv2.Canny(img, minVal, maxVal)
    cv2.imshow('edges', edges)

back = np.zeros((10, 10, 3), dtype=np.uint8)
cv2.namedWindow('image')
cv2.createTrackbar('minVal', 'image', 0, 255, canny)
cv2.createTrackbar('maxVal', 'image', 0, 255, canny)

while(1):
    cv2.imshow('image', back)
    k = cv2.waitKey(1) & 0xFF
    if k==27:
        break

cv2.destroyAllWindows()