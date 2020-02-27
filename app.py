from flask import Flask, render_template, Response, request, redirect, url_for
from sample import run
from markov import *

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    with open("ht.txt", 'r') as f:
        words = f.read()
    dic = Markogram(words.split(), order=3)
    msg = ' '.join(run())
    msg2 = dic.get_string(20)
     
    return render_template('index.html', msg=msg, msg2=msg2)

if __name__ == "__main__":
    app.run(debug=True)