from flask import Flask
from flask_restful import Resource, Api
from os import environ
import pymysql

conn = pymysql.connect(
    host=environ.get('host'), port=environ.get('port',3306), user=environ.get('user'),
    passwd=environ.get('passwd'), db=environ.get('db')
)

app = Flask(__name__)
api = Api(app)


class HelloWorld(Resource):
    def get(self):

        cursor = conn.cursor()
        cursor.execute(
            "SELECT count_view FROM view"
        )
        result =  cursor.fetchone()
        if result is None:
            cursor.execute(
            "INSERT INTO view VALUES (1)"
            )
        else:
            result = result[0] + 1
            cursor.execute(
            "UPDATE view set count_view = {}".format(result)
            )

        conn.commit()
        return result      

api.add_resource(HelloWorld, '/')


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=8080)
