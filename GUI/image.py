import cv2

def read_image(flag):
    """
    第2引数は画像の読み込み方法を指定するためのフラグです
    1 cv2.IMREAD_COLOR : カラー画像として読み込む．画像の透明度は無視される．デフォルト値
    0 cv2.IMREAD_GRAYSCALE : グレースケール画像として読み込む
    -1 cv2.IMREAD_UNCHANGED : アルファチャンネルも含めた画像として読み込む
    """
    img = cv2.imread('GUI/img/imori.jpg', flag)
    return img

out = read_image(-1)
cv2.imshow('result',out)
k = cv2.waitKey(0) # 何かキーを押したら終了

if k==27:
    cv2.destroyAllWindows() 
elif k==ord('s'): #ordで文字をASCIIに変換
    cv2.imwrite('GUI/img/imori_out.jpg', out)
    cv2.destroyAllWindows() 
