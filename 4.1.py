S = int(input("Введите сумму S: "))

a = [5000, 1000, 500, 100, 50, 10]
counts = {}

for sosik in a:
    if S >= sosik:
        counts[sosik] = S // sosik
        S %= sosik

print("Количество купюр:")
for sosik, count in counts.items():
    print(f"{sosik} руб.: {count} шт.")
