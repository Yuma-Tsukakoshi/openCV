import cv2
import numpy as np

# 画像のブレンド
img1 = cv2.imread('primitive_operation/img/imori.jpg')
img2 = cv2.imread('primitive_operation/img/canny_erode2.jpg')

# 重みの設定
dst = cv2.addWeighted(img1, 0.6, img2, 0.4, 0)

# cv2.imshow('dst', dst) 
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# =============================================================================
# ビット単位の操作　画像中の特定の領域を切り出すために使う

img1 = cv2.imread('primitive_operation/img/thorino.jpg')
img2 = cv2.imread('primitive_operation/img/logo.png')
img2 = cv2.resize(img2, (128, 128))

rows, cols, channels = img2.shape
roi = img1[0:rows, 0:cols]

# 画像をグレースケールに変換
img2gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

# ret: 閾値、mask: 2値化した画像 10,255: 閾値の範囲
ret, mask = cv2.threshold(img2gray, 10, 255, cv2.THRESH_BINARY)
mask_inv = cv2.bitwise_not(mask) # 黒：0, 白：1　から　黒：1, 白：0　に変換

# 黒い部分で切り抜き(logoの部分だけ黒)→白い部分で切り抜き(logoのみ)→重ねる
# 画像の黒い部分を切り抜く 
img1_bg = cv2.bitwise_and(roi, roi, mask=mask_inv)
cv2.imshow('img1_bg', img1_bg)

# 画像の白い部分を切り抜く
img2_fg = cv2.bitwise_and(img2, img2, mask=mask)
cv2.imshow('img2_fg', img2_fg)

# 画像を重ねる
dst = cv2.add(img1_bg, img2_fg)
cv2.imshow('dst', dst)
img1[0:rows, 0:cols] = dst

cv2.imshow('res', img1)
cv2.waitKey(0)
cv2.destroyAllWindows()
