from flask import Flask, render_template, Response, request, redirect, url_for
from sample import run

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    msg = ' '.join(run())
     
    return render_template('index.html', msg=msg)

if __name__ == "__main__":
    app.run(debug=True)