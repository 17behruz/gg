def format_text(text):
    sentences = text.split('.')
    formatted_text = ''

    for sentence in sentences:
        sentence = sentence.strip()
        if sentence:
            formatted_text += sentence[0].upper() + sentence[1:] + '. '  # Первая буква заглавная
    return formatted_text.strip()


text2 = input("Введите текст: ")
print("Отформатированный текст:", format_text(text2))