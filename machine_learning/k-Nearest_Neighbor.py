"""
K近傍法: k-Nearest Neighbor
- 未知のデータに対して、既知のデータの中から最も近いk個のデータを選び、多数決で分類する手法
- kは奇数で選ぶことが良い! (偶数だと同数票になることがあるため)

ただ多数決で決めるのではなく、距離に重みをつける必要が出てくる
modifed_kNNで実装: 重み付きk-Nearest Neighbor

<必要なこと>
地図上の全データを取得する必要がある
→ 距離を知る必要があるため
"""

import cv2 
import numpy as np
import matplotlib.pyplot as plt

trainData = np.random.randint(0, 100, (25, 2)).astype(np.float32)

responses = np.random.randint(0,2,(25,1)).astype(np.float32)

red = trainData[responses.ravel()==0]
plt.scatter(red[:,0], red[:,1], 80, 'r', '^')

blue = trainData[responses.ravel()==1]
plt.scatter(blue[:,0],blue[:,1], 80, 'b', 's')

newcomer = np.random.randint(0,100,(1,2)).astype(np.float32)
plt.scatter(newcomer[:0], newcomer[:1], 80, 'g', 'o')

knn = cv2.KNearest()
knn.train(trainData, responses)
ret, results, neighbours, dist = knn.find_nearest(newcomer, 3) 

print("result: ", results,"\n")
print("neighbours: ", neighbours,"\n")
print("distance: ", dist)

plt.show()