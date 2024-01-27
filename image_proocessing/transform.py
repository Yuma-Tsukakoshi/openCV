import cv2 
import numpy as np

# スケール変換 2倍
# 第2引数は出力画像のサイズ　Noneでfx,fyを指定する必要がある Interpolationは補間方法
img = cv2.imread('img/imori.jpg')
res = cv2.resize(img, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)

# 並進
"""
cv2.warpAffine は2x3の変換行列を入力する
cv2.warpPerspective は3x3の変換行列を入力とします
"""
img = cv2.imread('img/imori.jpg', 0)
rows , cols = img.shape
M = np.float32([[1, 0, 100], [0, 1, 50]])
# 第３引数は出力画像のサイズ
dst = cv2.warpAffine(img, M, (cols, rows))

# 回転
# 第1引数は回転の中心座標、第2引数は回転角度、第3引数はスケール
M = cv2.getRotationMatrix2D((cols/2, rows/2), 90, 1)
dst = cv2.warpAffine(img, M, (cols, rows))

# アフィン変換　並行性を保つ変換
img = cv2.imread('img/imori.jpg')
rows, cols, ch = img.shape

# 変換前後の座標を指定　3点必要
pts1 = np.float32([[50, 50], [200, 50], [50, 200]])
pts2 = np.float32([[10,100],[200,50],[100,250]])

M = cv2.getAffineTransform(pts1, pts2)
dst = cv2.warpAffine(img, M, (cols, rows))

# 射影変換 4点必要
pts1 = np.float32([[56,65],[368,52],[28,387],[389,390]])
pts2 = np.float32([[0,0],[300,0],[0,300],[300,300]])

M = cv2.getPerspectiveTransform(pts1, pts2) 
dst = cv2.warpAffine(img,M,(300,300))

