import cv2 
import numpy as np

"""
輪郭の特徴
"""
img = cv2.imread('img/imori.jpg', 0)
# ret: 閾値, thresh: 2値化した画像
ret, thresh = cv2.threshold(img, 127, 255, 0)
# imgEdge: 輪郭のみの画像, contours: 輪郭の座標, hierarchy: 階層構造

contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# contours[輪郭番号][点の番号][0][X座標, Y座標]
cnt = contours[0]

# # モーメント
M = cv2.moments(cnt)

# 重心
cx = int(M['m10']/M['m00'])
cy = int(M['m01']/M['m00'])

# 面積
area = cv2.contourArea(cnt)

# 周囲長 True:閉曲線, False:開曲線
perimeter = cv2.arcLength(cnt,True)

# 輪郭の近似 ex)崩れた長方形を長方形に近似する
epsilon = 0.1*cv2.arcLength(cnt,True)  # 輪郭の周囲長の10%を閾値とする
approx = cv2.approxPolyDP(cnt,epsilon,True)

# 凸包 TrueかFalseで凸包かどうかを指定
k=cv2.isContourConvex(cnt)
# 外接矩形
#a: 物体を囲む長方形を描画する
x,y,w,h = cv2.boundingRect(cnt)
img = cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
#b:　物体を囲む最小の長方形を描画する 回転を考慮
rect = cv2.minAreaRect(cnt)
box = cv2.boxPoints(rect) # 四隅の座標を取得
box = np.int0(box) # 整数に変換
img = cv2.drawContours(img,[box],0,(0,0,255),2)

# 最小外接円
(x,y),radius = cv2.minEnclosingCircle(cnt)
center = (int(x),int(y))
radius = int(radius)
img = cv2.circle(img,center,radius,(0,255,0),2)

# 楕円フィッティング
ellipse = cv2.fitEllipse(cnt) # 楕円の中心(x,y), (長軸, 短軸), 回転角度を返す
img = cv2.ellipse(img,ellipse,(0,255,0),2)

# 直線のフィッティング  
rows,cols = img.shape[:2]
[vx,vy,x,y] = cv2.fitLine(cnt, cv2.DIST_L2,0,0.01,0.01)
lefty = int((-x*vy/vx) + y)
righty = int(((cols-x)*vy/vx)+y)
img = cv2.line(img,(cols-1,righty),(0,lefty),(0,255,0),2)

