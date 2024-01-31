"""
コーナーの検出は画像の特徴を抽出するための重要なステップである．
画像中の小領域を見て，その周囲の領域で微小な移動を加えた時に最大の分散を示す領域を見つける

Feature Description : 特徴量記述
→ 同じ特徴量を見つけることができたり共通する特徴てんを基に画像をつなげたりできる


固有値によって、対象領域がコーナ、エッジ、フラットのどれに属するかを判定する
Rの値が重要; R = det(M) - k(trace(M))^2 (trace; λ1 + λ2)
"""
import cv2 
import numpy as np

img = cv2.imread('img/thorino.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

gray = np.float32(gray)
dst = cv2.cornerHarris(gray, 2, 3, 0.04) # 2: ブロックサイズ, 3: Sobelフィルタのカーネルサイズ, 0.04: ハリスコーナー検出器の自由パラメータ
dst = cv2.dilate(dst, None) # 膨張処理 画像中の白い部分を増やす 内部のノイズ除去
img[dst>0.01*dst.max()] = [0, 0, 255] # しきい値を設定

cv2.imshow('dst', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# =============================================================================
ret, thresh = cv2.threshold(dst, 0.01*dst.max(), 255, 0) # 2値化
dst = np.uint8(dst)

ret, labels, stats, centroids = cv2.connectedComponentsWithStats(dst) # ラベリング処理
# define the criteria to stop and refine the corners
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 100, 0.001)
corners = cv2.cornerSubPix(gray,np.float32(centroids),(5,5),(-1,-1),criteria)

# Now draw them
res = np.hstack((centroids,corners))
res = np.int0(res)
img[res[:,1],res[:,0]]=[0,0,255]
img[res[:,3],res[:,2]] = [0,255,0]

cv2.imshow('result',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

