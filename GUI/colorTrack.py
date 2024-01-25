import cv2
import numpy as np

drawing = False 

def nothing(x):
    pass

# mouse callback function
def draw_circle(event,x,y,flags,param):
    global drawing, palette, size, b, g, r 

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True

    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing == True:
            cv2.circle(img,(x,y),size,(b,g,r),-1)

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        cv2.circle(img,(x,y),size,(b,g,r),-1)


img = np.full((512, 512, 3), (255, 255, 255), dtype=np.uint8)
cv2.namedWindow('image')
# setMouseCallback: マウスイベントが発生するたびに関数draw_circleが呼び出される
cv2.setMouseCallback('image', draw_circle)  

# トラックバー名、ウィンドウ名、初期値、最大値、コールバック関数(今回は何もしない)
cv2.createTrackbar('R','image',0,255,nothing)  
cv2.createTrackbar('G','image',0,255,nothing)  
cv2.createTrackbar('B','image',0,255,nothing)  
cv2.createTrackbar('Size','image',0,10,nothing)  

while(1):
    cv2.imshow('image', img)
    k = cv2.waitKey(1) & 0xFF
    if k==27:
        break
    
    # getTrackbarPos: スライダーの現在の位置を取得
    r = cv2.getTrackbarPos('R','image')  
    g = cv2.getTrackbarPos('G','image')  
    b = cv2.getTrackbarPos('B','image')  
    size = cv2.getTrackbarPos('Size','image')  

    # 画像の色と同じだったから上手く見えなかった
    # img[:] = [b,g,r]

cv2.destroyAllWindows()