import cv2 
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('img/imori.jpg',0)
# 第二引数：グレースケールのため[0]
hist = cv2.calcHist([img], [0], None, [256], [0, 256])

# ravel(): 多次元配列を1次元配列に変換する 
hist, bins = np.histogram(img.ravel(), 256, [0, 256])

# ビンごとの計算はnp.bincount()を使った方が高速
hist = np.bincount(img.ravel(), minlength=256)

img = cv2.imread('img/imori.jpg')
color = ('b','g','r')
for i,col in enumerate(color):
    # 第二引数：グレースケールのため[0]
    histr = cv2.calcHist([img],[i],None,[256],[0,256])
    plt.plot(histr, color = col)
    plt.xlim([0,256])
plt.show()
    
plt.hist(img.ravel(),256,[0,256]); plt.show()

#maskを作成する場合
mask = np.zeros(img.shape[:2], np.uint8)
mask[50:100, 50:100] = 255
masked_img = cv2.bitwise_and(img, img, mask=mask)

hist_full = cv2.calcHist([img],[0], None, [256], [0,256])
hist_mask = cv2.calcHist([img],[0], mask, [256], [0,256])

plt.subplot(221), plt.imshow(img, 'gray')
plt.subplot(222), plt.imshow(mask,'gray')
plt.subplot(223), plt.imshow(masked_img, 'gray')
plt.subplot(224), plt.plot(hist_full), plt.plot(hist_mask)
plt.xlim([0,256])

plt.show()