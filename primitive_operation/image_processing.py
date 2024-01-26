import cv2 
import numpy as np

img = cv2.imread('primitive_operation/img/imori.jpg')
px = img[100, 100]

blue = img[100, 100, 0] #bgr
green = img[100, 100, 1]
red = img[100, 100, 2] 

img[100, 100] = [255, 255, 255] # 画素の変換

#============================================

img.item(10, 10, 2) # 10, 10のRの値を取得
img.itemset((10, 10, 2), 100) # 10, 10のRの値を100に変更

#============================================

print(img.shape) # (128, 128, 3) 128x128のカラー画像
print(img.size) # 49152 128x128x3
print(img.dtype) # uint8

#============================================
# ROI(Region of Interest)
eye = img[64:84, 64:84]
img[23:43, 30:50] = eye
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

#============================================
b,g,r = cv2.split(img) # BGR -> B, G, R splitは処理が重いのでnumpyのインデックスを使った方が良い
img = cv2.merge((b,g,r)) # B, G, R -> BGR

b = img[:,:,0]

#=============================================================================
# 画像のpadding
"""
引数：
img
top, bottom, left, right 幅決める
borderType: cv2.BORDER_CONSTANT, cv2.BORDER_REPLICATE, cv2.BORDER_REFLECT, cv2.BORDER_WRAP, cv2.BORDER_REFLECT_101
""" 

