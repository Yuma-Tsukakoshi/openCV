"""
mean_shit: 対象領域を囲み、点群の重心と円の中心が重なるまで移動を続けて物体を追跡する
"""

import cv2
import numpy as np

cap = cv2.VideoCapture('Video_analysis/slow.flv')
print(cap.isOpened())
ret, frame = cap.read()

r,h,c,w = 250, 90, 400, 125
track_window = (c,r,w,h) #c:x , r:y

# roi: 部分処理
roi = frame[r:r+h, c:c+w]
hsv_roi = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
mask = cv2.inRange(hsv_roi, np.array((0.,60.,32.)), np.array((180, 255., 255.)))
roi_hist = cv2.calcHist([hsv_roi],[0],mask,[180],[0,180])
cv2.normalize(roi_hist, roi_hist, 0,255, cv2.NORM_MINMAX)

term_crit = ( cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 1)

while(1):
    ret, frame = cap.read()
    
    if ret == True:
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        dst = cv2.calcBackProject([hsv], [0], roi_hist, [0, 180], 1)
        
        ret, track_window = cv2.meanShit(dst, track_window, term_crit)
        
        x,y,w,h = track_window
        img2 = cv2.rectangle(frame, (x,y), (x+w,y+h), term_crit)
        cv2.imshow('img2', img2)
        
        k = cv2.waitKey(60) & 0xff
        if k == 27:
            break
        else:
            cv2.imwrite(chr(k)+".jpg", img2)
    else:
        break

cv2.destroyAllWindows()
cap.release()