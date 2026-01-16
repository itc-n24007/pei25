list_date = [1, 9, 9, 1, 2, 7]
print(max(list_date) >= min(list_date) * 5)

month = ''
day = ''
for i in list_date[4:5]:
    month += str(i)
for i in list_date[-1:]:
    day += str(i)
print(f'{month:0>2}月 {day:0>2}日')

list_a = []
for i in list_date:
    list_a.append(-i)

print(list_a)

list_b = []
list_c = list_date[::-1]
index = 0
while index < len(list_date):
    list_b.append(list_date[index] + list_c[index])
    index += 1
print(list_b)

total = sum(list_date)
