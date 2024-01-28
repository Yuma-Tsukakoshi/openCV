import cv2
import numpy as np

"""
輪郭は二値画像を仮定している→白：物体, 黒：背景
"""

im = cv2.imread('img/imori.jpg')
imgray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
ret,thresh = cv2.threshold(imgray,127,255,0)

# 検出した輪郭を描画する drawContours で描画する
# 第３引数：輪郭の近似方法を指定している→メモリの使用を抑えられる
image, contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

img = cv2.drawContours(image, contours, -1, (0,255,0), 3)
img = cv2.drawContours(img, contours, 3, (0,255,0), 3)

cnt = contours[4]
img = cv2.drawContours(img, [cnt], 0, (0,255,0), 3)