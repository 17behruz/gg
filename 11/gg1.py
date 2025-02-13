def count_words_starting_with_b(text):
    words = text.split()
    count = sum(1 for word in words if word.lower().startswith('b'))
    return count

text1 = input("Введите текст: ")
print("Количество слов, начинающихся с буквы 'b':", count_words_starting_with_b(text1))