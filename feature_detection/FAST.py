"""
FAST アルゴリズム:
→ 画像の各ピクセルに対して、周囲の16ピクセルを見て、
IpをもとにIp+t, Ip-tの閾値を超える点が連続しているかを見る
→ 全ての点で閾値を超えている場合、その点をコーナーとして認識する

決定木を使って画像のコーナーを高速に検出することができる
"""

import cv2
import numpy as np

img = cv2.imread('img/thorino.jpg', 0)

fast = cv2.FastFeatureDetector()

kp = fast.detect(img, None)
img2 = cv2.drawKeypoints(img, kp, color=(255,0,0))

# 閾値、非最大値抑制、neighborhoodの値を表示
print('Threshold:', fast.getInt('threshold'))
print('NonmaxSuppression:', fast.getBool('nonmaxSuppression'))
print('neighborhood:', fast.getInt('type'))
print('Total Keypoints with nonmaxSuppression:', len(kp))

cv2.imwrite('fast_true.png', img2)

# NonmaxSuppressionは、閾値を超えた点の中で最大のものだけを残すかどうかを決める 点が重なっている場合に使う
fast.setBool('nonmaxSuppression', 0)
kp = fast.detect(img, None)

print('Total Keypoints without nonmaxSuppression:', len(kp))

img3 = cv2.drawKeypoints(img, kp, color=(255,0,0))

cv2.imwrite('fast_false.png', img3)