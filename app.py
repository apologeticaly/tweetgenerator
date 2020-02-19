from flask import Flask
from simple_sample import run
app = Flask(__name__)

if __name__ == "__main__":
    @app.route('/')
    def hello_world():
        return ' '.join(run())