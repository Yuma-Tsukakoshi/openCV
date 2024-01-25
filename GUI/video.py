import cv2

def read_video():
    cap = cv2.VideoCapture(0) # 引数はカメラのデバイス番号
    while True:
        ret, frame = cap.read() # retは画像を取得成功フラグ
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow('frame',gray)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()
    return 

read_video()
