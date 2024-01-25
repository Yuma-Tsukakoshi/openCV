"""
共通する引数：
img
color : BGR
thickness : 線の太さ
"""

import numpy as np
import cv2

# 512x512の3チャンネル画像を作成
img = np.zeros((512,512,3), dtype=np.uint8)

def draw_figure(img):
    # 左上と右下の座標を引数に取る
    img = cv2.line(img,(0,0),(511,511),(255,0,0),5)
    img = cv2.rectangle(img,(384,0),(510,128),(0,255,0),3)
    
    # 中心座標と半径を引数に取る -1:で塗りつぶし
    img = cv2.circle(img,(447,63), 63, (0,0,255), -1)
    
    # 中心座標・（長径・短径）・回転角度・円弧の開始角度・円弧の終了角度・色・線の太さ
    img = cv2.ellipse(img,(256,256),(100,50),0,0,180,(255,0,0),-1)
    
    # 多角形の頂点座標を引数に取る
    pts = np.array([[10,5],[20,30],[70,20],[50,10]], np.int32)
    pts = pts.reshape((-1,1,2))
    # true: 始点と終点を結ぶ線を引く
    img = cv2.polylines(img,[pts],True,(0,255,255))
    
    # 画像にテキストを描画
    font = cv2.FONT_HERSHEY_SIMPLEX # フォントの指定
    # 文字列・座標・フォント・フォントサイズ・色・線の太さ・線の種類
    img = cv2.putText(img, 'OpenCV', (10,500), font, 4, (255,255,255), 2, cv2.LINE_AA)
    return img

def draw_logo(img):
    img = cv2.circle(img,(256, 150), 63, (0,0,255), 50)
    img = cv2.circle(img,(156,310), 63, (0,255,0), 50)
    img = cv2.circle(img,(356,310), 63, (255,0,0), 50)
    img = cv2.ellipse(img,(256, 150),(90, 90),60,0,60,(0,0,0),-1)
    img = cv2.ellipse(img,(156, 310),(90, 90),-60,0,60,(0,0,0),-1)
    img = cv2.ellipse(img,(356, 310),(90, 90),240,0,60,(0,0,0),-1)
    
    font = cv2.FONT_HERSHEY_SIMPLEX # フォントの指定
    img = cv2.putText(img, 'OpenCV', (80,480), font, 3, (255,255,255), 10, cv2.LINE_AA)
    
    return img

# out = draw_figure(img)
out = draw_logo(img)
cv2.imshow('result', out)
cv2.imwrite('GUI/img/logo.png', out)
cv2.waitKey(0) 
cv2.destroyAllWindows()