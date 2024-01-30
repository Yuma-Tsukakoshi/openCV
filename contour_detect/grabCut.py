# GrabCutを使った対話的前景領域抽出

"""
前景と背景の領域を分割して前景領域を抽出する手法
¬ 初期値である矩形領域を指定
¬ その矩形領域内の前景と背景を指定
¬ その指定を元に前景と背景の領域を分割
¬ 分割された領域を元に前景領域を抽出
ユーザーの入力によって、都度修正を加えていく

画素値の分布からグラフを構築します．
グラフのノードは画素に Source と Sink を加えたものになります
全ての前景画素はSourceノードに連結され全ての背景画素はSinkノードに連結されます
→前景らしさと背景らしさを表現する
→mincutアルゴリズムを用いて、前景と背景の領域を分割する
→識別処理が収束するまで処理を繰り返す
"""

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('img/ice1.png')
mask = np.zeros(img.shape[:2], np.uint8)

# 内部のアルゴリズムで使う変数
bgdModel = np.zeros((1, 65), np.float64)
fgdModel = np.zeros((1, 65), np.float64)

rect = (180,300,400,500)
cv2.grabCut(img, mask, rect, bgdModel, fgdModel, 5, cv2.GC_INIT_WITH_RECT)

# 0:背景, 2:背景に含まれる可能性 
mask2 = np.where((mask==2)|(mask==0), 0, 1).astype('uint8') 
img = img*mask2[:,:,np.newaxis]

plt.imshow(img)
plt.colorbar()
plt.show()

