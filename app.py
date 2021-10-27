from flask import Flask, render_template, send_from_directory

app = Flask(__name__, static_url_path='')


@app.route('/')
def home():
    return send_from_directory(app.static_folder, 'Home.html')


@app.route('/text')
def text():
    return send_from_directory(app.static_folder, 'Text.html')
