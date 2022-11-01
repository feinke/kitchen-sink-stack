# from flask import Flask, jsonify
# from pytube import YouTube

# app = Flask(__name__)

# @app.route('/')
# def hello_world():
#     return 'Hello, Docker!'

# @app.route('/<id>')
# def getTheId(id):
#     yt = YouTube(f'https://youtu.be/{id}')
#     print(yt.streams.get_audio_only())
#     return 'ok1'
    # return yt.streams.filter(only_audio=True).first().download()
    # return f'Hello, tsssest {id}!'
