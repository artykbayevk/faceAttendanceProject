from flask import Flask
import requests

app = Flask(__name__)


@app.route('/')
def hello_world():
    files = {
        'photo[0] ': (None, ' ~/kamalsdu/Desktop/img1.jpg'),
        'photo[1] ': (None, ' ~/kamalsdu/Desktop/img2.jpg'),
    }

    response = requests.post('https://verigram.kz/api/', files=files)
    return response.data


if __name__ == '__main__':
    app.run()
