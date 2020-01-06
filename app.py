from flask import Flask
from flask_restful import Resource, Api
import pymysql

conn = pymysql.connect(
    host="localhost", port=3306, user="root",
    passwd="i234", db="page_view"
)

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

api.add_resource(HelloWorld, '/')

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=8080)
