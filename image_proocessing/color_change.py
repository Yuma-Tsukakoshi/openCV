import cv2
import numpy as np

# img = cv2.imread('img/imori.jpg')

# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# # 他にも：　cv2.COLOR_BGR2HSVなどもある

# cv2.imshow('img', gray)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# =============================================================================
# 物体追跡

cap = cv2.VideoCapture(0)
# カメラを起動してリアルタイムで取得する

while True:
    _, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    # HSVで指定した色の範囲を抽出する
    lower_blue = np.array([110, 50, 50])
    upper_blue = np.array([130, 255, 255])
    
    # 範囲内の色を抽出する → 2値化 
    mask = cv2.inRange(hsv, lower_blue, upper_blue)
    
    res = cv2.bitwise_and(frame, frame, mask=mask)
    
    cv2.imshow('frame', frame)
    cv2.imshow('mask',mask)
    cv2.imshow('res', res)
    k=cv2.waitKey(5) & 0xFF
    if k==27:
        break

cv2.destroyAllWindows() 