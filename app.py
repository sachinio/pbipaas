#from __future__ import print_function

from flask import Flask
from flask import render_template
from flask import request
from flask import g

from flask import Flask
from flask.ext.pymongo import PyMongo

app = Flask(__name__)
mongo = PyMongo(app)


@app.route('/add/<name>')
def add(name=None):
    print mongo.db.user.insert_one({'name': name, 'power':'unknown power'})
    return 'ok'


@app.route('/hello/<name>')
def index(name=None):
    user = mongo.db.user.find_one_or_404({'name': name})
    print user
    return render_template('index.html', name=user['power'])


@app.route('/clear')
def clear(name=None):
    mongo.db.user.remove()
    return 'clear'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
