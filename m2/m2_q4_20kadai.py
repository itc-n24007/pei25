num = 5
list_b = []
while num < 26:
    for i in range(num, num+1):
        list_b.append(i)
    num += 2
print(sum(list_b))

