"""
背景差分：実世界では一つの画像や動画から対象となる物体のみを抽出したい
→ 後ろの背景を取り除くことが必要となってくる
→ 人とか車とかを検出するためには背景差分を使うことが多い
"""

import numpy as np
import cv2

cap = cv2.VideoCapture('vtest.avi')

# 3つのアルゴリズム
fgbg = cv2.createBackgroundSubtractorMOG()
fgbg = cv2.createBackgroundSubtractorMOG2()
fgbg = cv2.createBackgroundSubtractorGMG()


while(1):
    ret, frame = cap.read()

    fgmask = fgbg.apply(frame)

    cv2.imshow('frame',fgmask)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()

