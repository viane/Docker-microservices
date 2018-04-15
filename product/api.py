# Product Service

from flask import Flask
from flask import request
from flask_restful import Resource, Api
import time

app = Flask(__name__)
api = Api(app)


class Product(Resource):
    chat_log = []

    def get(self):
        current_time = time.localtime()
        chat_str = ' '
        chat_str += request.args['sender'] + ' : '
        chat_str += request.args['message']
        time_stamp = time.strftime('%d %b %Y %H:%M:%S', current_time)
        Product.chat_log.append(time_stamp + chat_str)
        return{
            'Chat Log': Product.chat_log
        }


api.add_resource(Product, '/')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
