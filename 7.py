def sort_and_count(arr):
    counter = 0
    n = len(arr)
    for i in range(1, n):
        j = i
        while j > 0 and arr[j - 1] > arr[j]:
            counter += 1
            # Меняем элементы местами
            arr[j - 1], arr[j] = arr[j], arr[j - 1]
            j -= 1
    return counter

# Пример использования
arr = [5, 3, 4, 1, 6, 2]
operations = sort_and_count(arr)
print(f"Отсортированный массив: {arr}")
print(f"Количество операций: {operations}")
