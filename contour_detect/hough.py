import cv2 
import numpy as np

img = cv2.imread('img/imori.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# apertureSize: ソーベルフィルタのサイズ
edge = cv2.Canny(gray, 50, 150, apertureSize=3)

# ハフ変換による直線検出 threshouldは直線とみなす最小の長さ=========
lines = cv2.HoughLines(edge, rho=1, theta=np.pi/180, threshold=200 )

# ハフ変換による円検出==========================================
img = cv2.imread('img/logo.png',0)
img = cv2.medianBlur(img,5) # ぼやかす
cimg = cv2.cvtColor(img,cv2.COLOR_GRAY2BGR) # グレースケールからBGRに変換
# dp: 精度の逆数, minDist: 検出した円の中心同士の最小距離, param1: Canny法の上限, param2: 中心点の閾値 検出の可否を決める
circles = cv2.HoughCircles(img, cv2.HOUGH_GRADIENT, dp=0.3, minDist=20, param1=50, param2=30, minRadius=0, maxRadius=0)
# 返り値：[x座標, y座標, 半径]の配列
circles = np.uint16(np.around(circles))


for i in circles[0,:]:
    cv2.circle(cimg, (i[0], i[1]), i[2],(0,255,0), 2)
    cv2.circle(cimg, (i[0], i[1]), 2,(0,0,255), 3) # 中心点に赤い印を描画

# cv2.imshow('detect_circle', cimg)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
    