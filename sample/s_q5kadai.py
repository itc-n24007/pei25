list_a = [5, 12, 7, 12, 20]

list_b = list_a.copy()
list_b.remove(12)
list_b.insert(1, 99)  
list_b.append(0)

print("list_a:", list_a)
print("list_b:", list_b)

