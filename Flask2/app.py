from flask import Flask, render_template, request, redirect, url_for
import json
from googletrans import Translator  # Установите библиотеку: pip install googletrans==4.0.0-rc1

app = Flask(__name__)

# Зеленый уровень: статический словарь
static_dict = {
    "hello": "привет",
    "world": "мир",
    "cat": "кот",
    "dog": "собака",
    "sun": "солнце"
}

# Красный уровень: загрузка истории из файла
HISTORY_FILE = "history.json"

def load_history():
    try:
        with open(HISTORY_FILE, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_history(history):
    with open(HISTORY_FILE, "w", encoding="utf-8") as file:
        json.dump(history, file, ensure_ascii=False, indent=4)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        text = request.form.get("text")
        lang = request.form.get("lang")

        # Желтый уровень: перевод через Google Translate
        translator = Translator()
        translation = translator.translate(text, dest=lang).text

        # Сохраняем историю (красный уровень)
        history = load_history()
        history.append({"text": text, "lang": lang, "translation": translation})
        save_history(history)

        return render_template("index.html", translation=translation, text=text, lang=lang)

    return render_template("index.html")

@app.route("/history")
def history():
    history = load_history()
    return render_template("history.html", history=history)

if __name__ == "__main__":
    app.run(debug=True)