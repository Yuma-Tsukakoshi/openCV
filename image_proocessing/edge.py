import cv2 
import numpy as np

img = cv2.imread('img/imori.jpg', 0)
laplacian = cv2.Laplacian(img,cv2.CV_64F)

# sobelx: 縦方向の輪郭を抽出　sobely: 横方向の輪郭を抽出
sobelx = cv2.Sobel(img,cv2.CV_64F,1,0,ksize=5)
sobely = cv2.Sobel(img,cv2.CV_64F,0,1,ksize=5)

# 画像の勾配を求める
# 画像の勾配とは、画像の各画素の輝度の変化の大きさを表す
