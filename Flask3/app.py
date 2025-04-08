from flask import Flask, request, g
import time
import logging

app = Flask(__name__)

# Настройка логирования
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

@app.before_request
def log_request_info():
    """
    Middleware для логирования информации о запросе.
    """
    g.start_time = time.time()  # Сохраняем время начала запроса
    logging.info(f"Запрос: {request.method} {request.url}")
    logging.info(f"Headers: {request.headers}")
    logging.info(f"Body: {request.get_data(as_text=True)}")

@app.after_request
def log_response_info(response):
    """
    Middleware для логирования информации об ответе.
    """
    duration = round(time.time() - g.start_time, 6)  # Вычисляем длительность запроса
    logging.info(f"Ответ: {response.status_code} ({duration} сек)")
    logging.info(f"Response Body: {response.get_data(as_text=True)}")
    return response

@app.route("/")
def index():
    return "Главная страница"

@app.route("/about")
def about():
    return "О нас"

if __name__ == "__main__":
    app.run(debug=True)