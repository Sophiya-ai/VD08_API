from flask import Flask, render_template
import requests
from bootstrap_flask import Bootstrap
# другой вариант подключения Bootstrap. на официальный сайт Bootstrap: [https://getbootstrap.com](https://getbootstrap.com).
#на главной странице выбераем версию Bootstrap, которую  хотим использовать
# На странице загрузки в секции "Compiled CSS and JS" кнопка для загрузки "Download".
# Качаем скомпилированные файлы Bootstrap, включая `bootstrap.min.css`

app = Flask(__name__)
Bootstrap(app) # подключаем Bootstrap
app.config['SECRET_KEY'] = 'your_secret_key'

#methods=['GET'] по умолчанию
@app.route('/')
def randomQuote():
    try:
        response = requests.get('https://api.quotable.io/random')
        response.raise_for_status()  # Проверка на ошибки HTTP
        data = response.json() #Извлекаем данные из JSON-ответа
        quote = data.get('content', 'Не удалось получить цитату')
        author = data.get('author', 'Неизвестный автор')
        return render_template('randomQuote.html', quote=quote, author=author)
    except requests.exceptions.RequestException as e:
        return f"Ошибка при запросе к API: {e}"


app.run(debug=True)