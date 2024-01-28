import cv2 
import numpy as np

img = cv2.imread('img/imori.jpg')
ret, thresh = cv2.threshold(img, 127, 255, 0)
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cnt = contours[0]

# アスペクト比
x,y,w,h = cv2.boundingRect(cnt)

# Extent: 外接矩形の面積に対する輪郭が占める面積の比
area = cv2.contourArea(cnt)
x,y,w,h = cv2.boundingRect(cnt)
rect_area = w * h
extent = float(area) / rect_area

# Solidity; 輪郭の面積に対する凸包の面積の比
area = cv2.contourArea(cnt)
hull = cv2.convexHull(cnt)
hull_area = cv2.contourArea(hull)
solidity = float(area) / hull_area

# 等価直径
area = cv2.contourArea(cnt)
equi_diameter = np.sqrt(4*area/np.pi)

# 傾き
(x,y),(MA,ma),angle = cv2.fitEllipse(cnt)

# マスクと画素点
mask = np.zeros(img.shape,np.uint8)
cv2.drawContours(mask,[cnt],0,255,-1)
pixelpoints = np.transpose(np.nonzero(mask))

# 最大値と最小値
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(img,mask = mask)

# 平均値
mean_val = cv2.mean(img,mask = mask)

# 端点
leftmost = tuple(cnt[cnt[:,:,0].argmin()][0])
rightmost = tuple(cnt[cnt[:,:,0].argmax()][0])
topmost = tuple(cnt[cnt[:,:,1].argmin()][0])
bottommost = tuple(cnt[cnt[:,:,1].argmax()][0])
