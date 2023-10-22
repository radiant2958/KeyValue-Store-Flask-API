from flask import Flask, request, jsonify
from flask_pymongo import PyMongo
from pymongo.errors import DuplicateKeyError
import logging
from model.model import KeyValue 


logging.basicConfig(filename="app.log", level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s")

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://mongo:27017/mydatabase"
mongo = PyMongo(app)

db_instance = KeyValue(mongo.db)

@app.route('/value', methods=['GET', 'POST', 'PUT'])
def manage_value():

    try:
        if request.method == 'POST':
            key = request.json.get('key')
            value = request.json.get('value')
            
            if not key or not value:
                return "Ключ или значение отсутствует!, 400"

            db_instance.add(key, value)
            return "Значение успешно добавлено!, 201"

        elif request.method == 'GET':
            key = request.args.get('key')

            if not key:
                return "Ключ или значение отсутствует!, 400"

            result = db_instance.get(key)
            if result:
                return jsonify({"value": result['value']})
            return jsonify({"message": "Ключ не найден!"}), 400


        elif request.method == 'PUT':
            key = request.json.get('key')
            new_value = request.json.get('value')

            if not key or not new_value:
                return "Ключ или значение отсутствует!, 400"

            db_instance.update(key, new_value)
            return "Значение успешно обновлено!, 200"

    except DuplicateKeyError:
        logging.error("Дублирование ключа. Ключ: %s", key)
        return "Ключ уже существует!, 400"
    except Exception as e:
        logging.error("Неожиданная ошибка: %s", str(e))
        return "Произошла неожиданная ошибка!, 500"
