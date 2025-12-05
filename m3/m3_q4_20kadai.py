def check_num(num):
    a = num[1]
    b = num[-1]
    c = len(num) == 919
    d = len(num) > 0

    print(f"変数aのtypeは{type(a)}")
    print(f"変数bのtypeは{type(b)}")
    print(f"変数cのtypeは{type(c)}")
    print(f"変数dのtypeは{type(d)}")

    if a == b and c and d:
        print(a * b)
    elif a == b or c or d:
        print(b * 2)


num = '919'
check_num(num)
