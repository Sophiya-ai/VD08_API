from flask import Flask, render_template, request
import requests

#импортируем объект класса Flask
app = Flask(__name__)

#формируем путь и методы GET и POST
@app.route('/', methods=['GET', 'POST'])
#создаем функцию с переменной weather, где мы будем сохранять погоду
def index():
   weather = None
#формируем условия для проверки метода.
   if request.method == 'POST':
#этот определенный город мы будем брать для запроса API
       city = request.form['city']
       weather = get_weather(city)
   return render_template("index.html", weather=weather)

def get_weather(city):
    api_key = '3b5252db69c6d077d131afdabfdd1f3e'
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
    response = requests.get(url)
    return response.json()

app.run(debug=True)