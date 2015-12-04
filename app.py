from __future__ import print_function

from flask import Flask
from flask import render_template
from flask import request
from flask import g

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')