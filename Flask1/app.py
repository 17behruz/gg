from flask import Flask, render_template

app = Flask(__name__)

rainbow_colors = [
    {"name": "Красный", "color": "#FF0000"},
    {"name": "Оранжевый", "color": "#FF7F00"},
    {"name": "Желтый", "color": "#FFFF00"},
    {"name": "Зеленый", "color": "#00FF00"},
    {"name": "Голубой", "color": "#00FFFF"},
    {"name": "Синий", "color": "#0000FF"},
    {"name": "Фиолетовый", "color": "#8B00FF"}
]

@app.route('/colors')
def colors():
    return render_template('colors.html', colors=rainbow_colors)

if __name__ == '__main__':
    app.run(debug=True)