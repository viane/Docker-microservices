# Product Service

from flask import Flask
from flask import request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


class Product(Resource):
    chat_log = []

    def get(self):
        chat_str = ''
        chat_str += request.args['sender'] + ' : '
        chat_str += request.args['message']
        Product.chat_log.append(chat_str)
        return{
            'Chat Log': Product.chat_log
        }


api.add_resource(Product, '/')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
