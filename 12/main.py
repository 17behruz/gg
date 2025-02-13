def has_universal_guest(students):
    # Создаем множество всех учеников
    all_students = set(students.keys())

    # Проверяем для каждого ученика, есть ли у него гость, который побывал у всех
    for student, guests in students.items():
        if all_students - {student} <= guests:
            return True
    return False


# Пример данных
students = {
    "Алексей": {"Мария", "Иван", "Ольга"},
    "Мария": {"Алексей", "Иван"},
    "Иван": {"Алексей", "Мария", "Ольга"},
    "Ольга": {"Алексей", "Иван"}
}

print(has_universal_guest(students))  # Вывод: True или False