from flask import Flask, render_template, Response, request, redirect, url_for
from simple_sample import run

app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello_world():
    return ' '.join(run())

if __name__ == "__main__":
    app.hello_world(debug=True)