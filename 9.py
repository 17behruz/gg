def print_arguments_and_functions(arr):
    n = len(arr) // 2
    print("Аргумент\tФункция")
    for i in range(n):
        print(f"{arr[i]}\t\t{arr[n + i]}")

# Пример использования
arr = [1, 2, 3, 10, 20, 30]
print_arguments_and_functions(arr)
