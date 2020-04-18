from flask import Flask
import firebase_admin
from firebase_admin import credentials, messaging

cred = credentials.Certificate("hackru-tester-firebase-adminsdk-jqagl-4e50aba4bc.json")
firebase_admin.initialize_app(cred)

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/announcement')
def send_announcement():
    message_title = "Announcement"
    message_body = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."
    message = messaging.Message(
        notification=messaging.Notification(
            title=message_title,
            body=message_body,
        ),
        topic="announcements",
    )
    response = messaging.send(message)
    return 'Announcement has been sent out'


if __name__ == '__main__':
    app.run()
