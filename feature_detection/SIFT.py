"""
SIFT: スケール変換に対応したコーナー検出アルゴリズム
極地点: キーポイント
1. 画像のスケール空間における極値点を検出する
2. 極値点の位置とスケールを決定する
3. 回転角の計算
4. 特徴点の向きを決定する
5. キーポイントのマッチング
"""

import cv2
import numpy as np

img = cv2.imread('img/thorino.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

sift = cv2.SIFT()
kp, des = sift.detectAndCompute(gray,None)

img = cv2.drawKeypoints(gray, kp,flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

cv2.imwrite('sift_keypoints.jpg', img)