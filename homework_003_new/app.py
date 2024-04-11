import time
import flask
from flask import Flask, abort
import random
from pydantic import BaseModel

class Message(BaseModel):
    name: str
    text: str
    data: dict

app = Flask(__name__)
db = []
for i in range(3):
    db.append({
        'name': 'Елизавета',
        'time': time.time(),
        'text': 'всем привет в этом чате!'
    })

game = False

@app.route("/")
def hello():
    return "Hi, this is my page!"

@app.route("/send", methods= ['POST'])
def send_message():
    '''
    функция для отправки нового сообщения пользователем
    :return:
    '''
    # TODO
    # проверить, является ли присланное пользователем правильным json-объектом
    # проверить, есть ли там имя и текст
    # Добавить сообщение в базу данных db
    data = flask.request.json

    if 'name' not in data or \
        'text' not in data:
        return abort(400)

    text = data['text']
    name = data['name']
    message = {
        'text': text,
        'name': name,
        'time': time.time()
    }
    db.append(message)


    predictions = ['Сомнительно', 'Думаю, мой ответ - да', 'Вряд ли', 'Попробуй спросить позже',
                   'Можешь попробовать', 'Точно нет', 'Скорее всего у тебя получится',
                   'Сосредоточься на вопросе и спроси еще раз', 'Вероятнее всего', 'Лучше не стоит']
    if text == '/predict':
        bot2 = random.randrange(0, 11)
        message = {
            'text': predictions[bot2],
            'name': 'Бот',
            'time': time.time()
        }
        db.append(message)

    return {'ok': True}

@app.route("/messages")
def get_messages():
    try:
        after = float(flask.request.args['after'])
    except:
        abort(400)
    db_after = []
    for message in db:
        if message['time'] > after:
            db_after.append(message)
    return {'messages': db_after}

@app.route("/status")
def print_status():
    users = []
    for i in db:
        if i['name'] not in users:
            users.append(i['name'])
    return {
        "firstName": "Елизавета",
        "lastName": "Попова",
        "address": {
            "streetAddress": "Рчзанский проспект",
            "city": "Москва",
            "postalCode": 490876
        },
        "phoneNumbers": "8(917)7900546",
        "all messages": len(db),
        "all users": len(users)
    }

@app.route('/index')
def lionel():
    return flask.render_template('index.html')


app.run()