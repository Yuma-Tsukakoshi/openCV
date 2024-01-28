import cv2 
import numpy as np

img = cv2.imread('img/imori.jpg')

kernel = np.ones((5,5),np.unit8)

# kernel内に1つでも0があれば、出力は0 1つでも1があれば、出力は1で収縮・膨張を行う
erosion = cv2.erode(img, kernel, iterations = 1)
dilation = cv2.dilate(img, kernel, iterations = 1)

# オープニング：収縮→膨張 対象物外のノイズを除去する
opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)

# クロージング：膨張→収縮　対象物内のノイズを除去する
closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)

# モルフォロジー勾配：膨張-収縮　差分をとって輪郭を抽出する
gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)

# トップハット：クロージング-元画像　明るい部分を抽出する　明るい部分が増えるから
tophat = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel)

# ブラックハット：元画像-オープニング　暗い部分を抽出する　暗い部分が増えるから
blackhat = cv2.morphologyEx(img, cv2.MORPH_BLACKHAT, kernel)
