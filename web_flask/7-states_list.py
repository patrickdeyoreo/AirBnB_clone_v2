#!/usr/bin/python3
'''
Start a Flask web application
'''
from models import storage
from models.state import State
from flask import Flask, render_template
app = Flask(__name__)

HOST = '0.0.0.0'
PORT = '5000'


@app.route('/states_list', strict_slashes=False)
def states_list():
    '''
    list states
    '''
    TEMPLATE = '7-states_list.html'
    return render_template(TEMPLATE, states=storage.all(State).values())


@app.teardown_appcontext
def close_storage(*args):
    '''
    close storage
    '''
    storage.close()


if __name__ == '__main__':
    app.run(host=HOST, port=PORT)
