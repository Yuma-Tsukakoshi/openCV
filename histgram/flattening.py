# ヒストグラム平坦化を行い画像のコントラストを上げる
# 突出して明るい画素を左右に広げて平坦化を行う

import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('img/imori.jpg', 0)

# revelとflattenの違い: flattenはコピーを作成する
hist, bins = np.histogram(img.flatten(), 256, [0, 256])

cdf = hist.cumsum() # 累積分布関数
cdf_normalized = cdf * hist.max() / cdf.max()

plt.plot(cdf_normalized, color = 'b')
plt.hist(img.flatten(),256,[0,256], color = 'r')
plt.xlim([0,256])
plt.legend(('cdf','histogram'), loc = 'upper left')
plt.show()


# OpenCVでのヒストグラム平坦化 すでに分布が広がっている場合は効果がない
equ = cv2.equalizehist(img)
res = np.hstack((img, equ)) # 結合 h:水平方向に結合 v:垂直方向に結合
cv2.imshow('res', res)

"""
適用的ヒストグラム平坦化: 分布がすでに広っがている場合に効果的になるようにする
画像を複数の小領域に分割し、その小領域ごとにヒストグラム平坦化を行う
cv2.createCLAHE(clipLimit, tileGridSize)
clipLimit: コントラスト制限の強さ 0~40 40がデフォルト 
tileGridSize: 画像を分割する領域サイズ
"""
clath = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
cl1 = clath.apply(img)

