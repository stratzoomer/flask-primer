from flask import Flask
from flask import send_file
from flask import request
import logging

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/api/v1/texttoasl/<path:letter>', methods=['POST'])
def text_to_asl_image(letter):
    ordinal = ord(letter)
    logging.info("Ordinal is {}   ", ordinal)
    return send_file('images/{}.gif'.format(ordinal))
