def count_numbers(n):
    count = 0
    for i in range(1, n+1):
        if i % 2 != 0 and i % 3 != 0 and i % 5 != 0:
            count += 1
    return count


n = int(input("Введите n: "))
print("Количество чисел:", count_numbers(n))