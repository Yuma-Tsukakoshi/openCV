import cv2 
import numpy as np


drawing = False # true if mouse is pressed
# mode = True # if True, draw rectangle. Press 'm' to toggle to curve
# ix,iy = -1,-1

"""
EVENT_LBUTTONDOWN: 左ボタンを押したとき
EVENT_MOUSEMOVE: マウスを動かしたとき
EVENT_LBUTTONUP: 左ボタンを離したとき
"""

# mouse callback function
def draw_circle(event,x,y,flags,param):
    # global ix,iy,drawing,mode
    global drawing

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        # ix,iy は　左クリックした座標
        # ix,iy = x,y

    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing == True:
            # if mode == True:
            #     cv2.rectangle(img,(ix,iy),(x,y),(0,255,0),-1)
            # else:
            cv2.circle(img,(x,y),5,(0,0,255),-1)

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        # if mode == True:
        #     cv2.rectangle(img,(ix,iy),(x,y),(0,255,0),-1)
        # else:
        cv2.circle(img,(x,y),5,(0,0,255),-1)

img = np.zeros((512,512,3), np.uint8)
cv2.namedWindow('image')
# setMouseCallback: マウスイベントが発生するたびに関数draw_circleが呼び出される
cv2.setMouseCallback('image',draw_circle)

while(1):
    cv2.imshow('image',img)
    k = cv2.waitKey(1) & 0xFF
    if k==27:
        break
    # if k == ord('m'):
    #     mode = not mode
    # elif k == 27:
    #     break

cv2.destroyAllWindows()

