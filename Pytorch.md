# 1_1_tensor_tutorial
- テンソル型　- numpy型　に変更可能
→ GPU で高速演算処理可能になる

- テンソル そのものの変更 (in-place)
y.add_(x) → メソッド名の後に_をつけることで変数の内容を置換できる
基本は新たにコピーして変数に入る

- tensor リサイズ
.resize → .view で定義するでリサイズする

- NumPyとの接続 Tensor → numpy
TensorとNumpyのメモリは共有されてる  
a = torch.ones(5)  
b = a.numpy()  
a.add_(1) → 足したら両方とも加算する

- NumPy →　Tensor　へ変換
a = np.ones(5)  
b = torch.from_numpy(a)  
np.add(a, 1, out=a)  

# 1_2_autograd_tutorial
- requires_grad
計算結果の履歴を追跡して.grad_fn属性で作成したFunctionを参照

- backward()
誤差逆伝播法の実行

- grad
勾配の計算



