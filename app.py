from flask import Flask
import firebase_admin
from firebase_admin import credentials, messaging

cred = credentials.Certificate("hackru-tester-firebase-adminsdk-jqagl-4e50aba4bc.json")
firebase_admin.initialize_app(cred)

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
