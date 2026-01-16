a = 0b101100
b = 0b110110
c = []

c.append(bin(a & b).count('1'))
c.append(bin(a | b).count('1'))
c.append(bin(a ^ b).count('1'))
c.append(bin(a >> 2).count('1'))
print(c)
