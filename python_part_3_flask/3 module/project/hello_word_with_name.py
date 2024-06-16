

from flask import Flask
import datetime

app = Flask(__name__)
week = ('Понедельника', 'Вторника', 'Среды', 'Четверга', 'Пятницы', 'Субботы', 'Воскресенья')
today = datetime.date.today()
week_day = today.weekday()

@app.route('/hello-world/<name>')
def hello_world(name):
    return f'Привет, {name}. Хорошей {week[week_day]}'


if __name__ == '__main__':
    app.run(debug=True)
