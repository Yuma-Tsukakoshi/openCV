import cv2 
import numpy as np

# 画像をぼかす平滑化フィルタ

# 2D コンボリューション(画像フィルタリング) 
img = cv2.imread('img/logo.png')
cv2.imshow('img', img)
kernel = np.ones((5,5),np.float32)/25

# -1: 入力画像と同じ深度
dst = cv2.filter2D(img,-1,kernel)

# 平均化
dst = cv2.blur(img,(5,5))

# ガウシアンフィルタ
dst = cv2.GaussianBlur(img,(5,5),0)

# メディアンフィルタ ごま塩ノイズを除去するのに有効
dst = cv2.medianBlur(img,5)
"""
バイラテラルフィルタ 輝度差が大きところに重みをつけてぼかす＝エッジを残す
エッジは、輝度が急激に変化する画素のこと
9: フィルタサイズ 
sigmaColor: 色についての標準偏差。これが大きいと、画素値の差が大きくても大きな重みが採用される。
sigmaSpace: 距離についての標準偏差。これが大きいと、画素間の距離が広くても大きな重みが採用される。
"""
dst = cv2.bilateralFilter(img,9,75,75)