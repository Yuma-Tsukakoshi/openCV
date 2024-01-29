import cv2 
import numpy as np
import matplotlib.pyplot as plt

"""
画像の領域分割や画像中の対象物体の検出に使われる
→ 対象：白 , それ以外：黒
カラー画像を見た方が定義しやすい
→ 各画素がグラウンドに属している確率を計算していくことで画像から対象物体を抽出する
"""

# numpy ========================================================
roi  = cv2.imread('img/flower.jpg')
hsv = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)

target = cv2.imread('img/template.jpg')
hsvt = cv2.cvtColor(target, cv2.COLOR_BGR2HSV)

# M = cv2.calcHist([hsv], [0, 1], None, [180, 256], [0, 180, 0, 256]) 
# I = cv2.calcHist([hsvt], [0, 1], None, [180, 256], [0, 180, 0, 256]) 
# R = M/I
# h,s,v = cv2.split(hsvt)
# B = R[h.ravel(), s.ravel()]
# B = np.minimum(B,1)
# B = B.reshape(hsvt.shape[:2])

# disc = cv2.getStructuringElment(cv2.MORPH_ELLIPSE, (5,5))
# cv2.filter2D(B, -1, disc, B)
# B = np.uint8(B)
# cv2.normalize(B, B, 0, 255, cv2.NORM_MINMAX)
# ret, thresh = cv2.threshold(B, 50, 255,0)

# openCV ========================================================

# calculating object histogram
roihist = cv2.calcHist([hsv],[0, 1], None, [180, 256], [0, 180, 0, 256] )

# normalize histogram and apply backprojection
cv2.normalize(roihist,roihist,0,255,cv2.NORM_MINMAX)
dst = cv2.calcBackProject([hsvt],[0,1],roihist,[0,180,0,256],1)

# Now convolute with circular disc
disc = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5))
cv2.filter2D(dst,-1,disc,dst)

# threshold and binary AND
ret,thresh = cv2.threshold(dst,50,255,0)
thresh = cv2.merge((thresh,thresh,thresh))
res = cv2.bitwise_and(target,thresh)

res = np.vstack((target,thresh,res))
cv2.imwrite('res.jpg',res)