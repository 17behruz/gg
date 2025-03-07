import task1
import task2
import task3

def main():
    print("Выберите задачу (1, 2, 3):")
    choice = int(input())
    
    if choice == 1:
        x = float(input("Введите x: "))
        result = task1.calculate_task1(x)
        print(f"Результат задачи 1: {result}")
    elif choice == 2:
        x = float(input("Введите x: "))
        result = task2.calculate_task2(x)
        print(f"Результат задачи 2: {result}")
    elif choice == 3:
        x = float(input("Введите x: "))
        n = int(input("Введите n: "))
        result = task3.calculate_task3(x, n)
        print(f"Результат задачи 3: {result}")
    else:
        print("Неверный выбор.")

if __name__ == "__main__":
    main()
