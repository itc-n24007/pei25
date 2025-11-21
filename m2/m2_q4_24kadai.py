def func(a, b):
    if a ** b <= 64:
        return 1
    else:
        return 0

# bool() は、0 を False、0 以外の数値を True として扱う関数
# 例: bool(1) → True, bool(0) → False

x = func(4, 3)
y = func(3, 4)
a = func(5, 6)

z = [bool(x), bool(y), bool(a)]
print(z)
