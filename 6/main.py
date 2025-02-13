def is_palindrome(n):
    return str(n) == str(n)[::-1]

def reverse_number(n):
    return int(str(n)[::-1])

def process_number(n):
    count = 0
    while not is_palindrome(n):
        reversed_n = reverse_number(n)
        n = n + reversed_n
        count += 1
        print(f"Шаг {count}: {n}")
    return n

# Ввод данных
n = int(input("Введите число: "))
result = process_number(n)
print(f"Полученный палиндром: {result}")