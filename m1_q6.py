# 50音表（や行・わ行の空白部は空文字）
hiragana_hyou = [
    ["あ", "い", "う", "え", "お"],
    ["か", "き", "く", "け", "こ"],
    ["さ", "し", "す", "せ", "そ"],
    ["た", "ち", "つ", "て", "と"],
    ["な", "に", "ぬ", "ね", "の"],
    ["は", "ひ", "ふ", "へ", "ほ"],
    ["ま", "み", "む", "め", "も"],
    ["や", "゛",  "ゆ", "゜",  "よ"],
    ["ら", "り", "る", "れ", "ろ"],
    ["わ", "っ",  "を",  "ー",  "ん"]
]

# (2) search_kana_idx関数
def search_kana_idx(kana):
    for i, row in enumerate(hiragana_hyou):
        for j, col in enumerate(row):
            if col == kana:
                return (i, j)
    return None

# (2) 暗号化処理
hirabun = input('ひらがなの文を入力してください: ')
codes = ""
for ch in hirabun:
    idx = search_kana_idx(ch)
    if idx is None:
        codes += "？"
    else:
        # 各インデックスを2桁で表現（例: 行3→"3" 列2→"2"）
        codes += f"{idx[0]}{idx[1]}"
print("暗号:", codes)

# (3) 復号処理
ango = input('暗号を入力してください: ')
if len(ango) % 2 != 0:
    print('暗号の文字数は偶数でなければなりません')
else:
    kanas = ""
    for i in range(0, len(ango), 2):
        row = int(ango[i])
        col = int(ango[i+1])
        if row >= len(hiragana_hyou) or col >= len(hiragana_hyou[row]) or hiragana_hyou[row][col] == "":
            kanas += "？"
        else:
            kanas += hiragana_hyou[row][col]
    print("復号結果:", kanas)

