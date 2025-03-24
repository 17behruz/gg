from flask import Flask

app = Flask(__name__)

@app.route('/colors')
def colors():
    rainbow_colors = [
        ("Красный", "#FF0000"),
        ("Оранжевый", "#FFA500"),
        ("Желтый", "#FFFF00"),
        ("Зеленый", "#008000"),
        ("Голубой", "#00BFFF"),
        ("Синий", "#0000FF"),
        ("Фиолетовый", "#8B00FF")
    ]
    
    html = "<h1>Цвета радуги</h1>"
    for color, hex_code in rainbow_colors:
        html += f'<p style="color: {hex_code}; font-size: 24px;">{color}</p>'
    
    return html

if name == '__main__':
    app.run(debug=True)
