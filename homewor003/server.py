# save this as app.py
import time
import flask
from flask import Flask, abort
from pydantic import BaseModel # Для пункта 3

app = Flask(__name__)
db = [
    {
        'time': time.time(),
        'name': 'Jack',
        'text': 'Привет всем!',
    },
    {
        'time': time.time(),
        'name': 'Mary',
        'text': 'Привет, Jack',
     }
]

class Message(BaseModel): # Для пункта 3
    name: str
    text: str

@app.route("/")
def hello():
    return "Hello, World! 123"

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
    try:
        message = Message(**data)
    except Exception as e:
        return abort(400, str(e))

    message_dict = message.dict()
    message_dict['time'] = time.time()
    db.append(message_dict)
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
def print_status(): # Пункт 1
    num_users = len(set([message['name'] for message in db]))
    num_messages = len(db)

    status_info = {
        "total_users": num_users,
        "total_messages": num_messages,
        "firstName": "Елизавета",
        "lastName": "Попова",
        "address": {
            "streetAddress": "ул. Рязанский проспект, 2/1, к3м",
            "city": "Москва",
            "postalCode": 450104
        }
    }
    return status_info

@app.route('/index')
def lionel(): 
    return flask.render_template('index.html')

@app.route("/commands", methods=['POST'])
def help_command(command): # Пункт 2
    if command == "\\help":
        return "Для отправки сообщения используйте метод '/send' с параметрами 'name' и 'text'. " \
               "Для получения информации о пользователе используйте GET запрос на /status. " \
               "Для получения списка сообщений после определенного времени используйте GET запрос на /messages с параметром 'after'."
    else:
        return "Неизвестная команда. Используйте '\\help' для просмотра списка команд."



app.run()