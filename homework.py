from flask import Flask, render_template
import requests
#import certifi
#библиотеку certifi чтобы гарантировать, что Python использует доверенные корневые сертификаты
# Установить библиотеку, если она у вас не установлена

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'


@app.route('/', methods=['GET'])
def randomQuote():
    try:
        #без verify возникла Ошибка SSLCertVerificationError: certificate verify failed: certificate has expired
        # при запросе к API https://api.quotable.io/random говорит о том, что возникли проблемы
        # с проверкой SSL-сертификата при подключении к серверу. Это означает, что компьютер (или среда,
        # в которой запущено приложение) не может должным образом проверить подлинность сертификата сервера api.quotable.io

        #response = requests.get('https://api.quotable.io/random', verify=certifi.where()) - указывает путь к сертификатам явно, но тут не пошел
        response = requests.get('https://api.quotable.io/random', verify = False) #Это небезопасный способ,
        # поскольку делает приложение уязвимым для атак “человек посередине”.
        # Использовать его нужно только для отладки и тестирования, но не в производственной среде

        response.raise_for_status()  # Проверка на ошибки HTTP
        data = response.json() #Извлекаем данные из JSON-ответа
        quote = data.get('content', 'Не удалось получить цитату')
        author = data.get('author', 'Неизвестный автор')
        return render_template('randomQuote.html', quote=quote, author=author)
    except requests.exceptions.RequestException as e:
        return f"Ошибка при запросе к API: {e}"


app.run(debug=True)