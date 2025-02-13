def count_unique_letters(text):
    # Используем множество для хранения уникальных букв
    unique_letters = set()

    # Проходим по каждому символу в тексте
    for char in text:
        if char.isalpha():  # Проверяем, является ли символ буквой
            unique_letters.add(char.lower())  # Добавляем букву в множество в нижнем регистре

    return len(unique_letters)


# Пример текста
text = "Слова в тексте разделены пробелами."
print(count_unique_letters(text))  # Вывод: количество уникальных букв