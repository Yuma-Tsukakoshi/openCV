import cv2
import numpy as np

# Watershedアルゴリズムを使った画像の領域分割
# 流れ出る水の分岐点を検出するアルゴリズム

img = cv2.imread('img/flower.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# 大津の二値化
ret, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

# オープニングを行い内部のノイズを削除
kernel = np.ones((3,3),np.uint8)
opening = cv2.morphologyEx(thresh,cv2.MORPH_OPEN,kernel, iterations = 2)

# 背景の領域を抽出
sure_bg = cv2.dilate(opening,kernel,iterations=3)

# 前景の領域を抽出 distanseTransformで距離を求める
dist_transform = cv2.distanceTransform(opening, cv2.DIST_L2, 5)
ret, sure_fg = cv2.threshold(dist_transform, 0.7*dist_transform.max(), 255, 0)

sure_fg = np.uint8(sure_fg)
unknown = cv2.subtract(sure_bg, sure_fg)

# Marker labelling
ret, markers = cv2.connectedComponents(sure_fg)

# Add one to all labels so that sure background is not 0, but 1
markers = markers+1

# Now, mark the region of unknown with zero
markers[unknown==255] = 0

markers = cv2.watershed(img,markers)
# imgで青く塗りつぶす
img[markers == -1] = [255,0,0]

cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows
