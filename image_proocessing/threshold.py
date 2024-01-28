import cv2
import numpy as np

img = cv2.imread('img/imori.jpg', 0)

# 127より大きい値は255、それ以外は0にする
ret, th = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
cv2.imshow('th', th)
cv2.waitKey(0)
cv2.destroyAllWindows()

#適応的閾値処理
# 領域ごとに閾値を変える必要がある

# kernelのサイズが5
"""
cv2.ADAPTIVE_THRESH_MEAN_C は、各領域の閾値をその周辺領域の平均値から計算
cv2.ADAPTIVE_THRESH_GAUSSIAN_C は、周辺領域の重み付け平均を使用して閾値を計算
ブロックサイズ=11
C = 2 。これにより、画像の異なる領域に適応的な閾値処理が適用
"""
img = cv2.medianBlur(img, 5)
ret, th1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
th2 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,\
            cv2.THRESH_BINARY,11,2)
th3 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
            cv2.THRESH_BINARY,11,2)

# 大津の二値化
# 双峰性を持つヒストグラムを持つ画像に対して、その双峰の間の値を閾値として適用する
img = cv2.imread('img/imori.jpg', 0)

ret1,th1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
# thresholdを0に設定する理由は、後述するOtsuのアルゴリズムでは、閾値を自動で計算するため
ret2,th2 = cv2.threshold(img,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

blur = cv2.GaussianBlur(img,(5,5),0)
ret3,th3 = cv2.threshold(blur,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)


