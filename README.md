n = int(input("Введите число доn: "))

res = 0
for i in range(1, n + 1):
    res += (i + 1) / i

print("результати:", res)
