"""
Shi-Tomasi corner detection
Harrisのコーナー検出の改良版
→ R = min(λ1, λ2) が大きいほどコーナーとして検出される
各コーナーについてスコアを計算し、スコアが高い順にコーナーを選択する
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('img/thorino.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

corners = cv2.goodFeaturesToTrack(gray, 30, 0.01, 10) # 100: 最大のコーナー数, 0.01: 最小のコーナー間隔, 10: コーナー間の最小ユークリッド距離
corners = np.int0(corners) # 整数に変換 コーナーの座標を取得
print(corners)

for i in corners:
    x, y = i.ravel() # 一次元配列に変換
    cv2.circle(img, (x, y), 3, 255, -1)

plt.imshow(img)
plt.show()