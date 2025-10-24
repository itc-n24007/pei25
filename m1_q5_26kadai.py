# 1. 変数aに2を代入
a = 2

# 空のリストを用意
list_a = []

# 2. aを使ってリストを作成（繰り返し処理）
for i in range(6):
    list_a.append(a)  # appendメソッドでリストの末尾にaの値を追加する（新しい要素を1つ加える）
    a *= 2  # aを2倍にして次のループで使う

# 結果を表示
print(list_a)
