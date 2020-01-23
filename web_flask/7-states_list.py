#!/usr/bin/python3
'''
Start a Flask web application
'''
from models import State, storage
from flask import Flask, render_template
app = Flask(__name__)

HOST = '0.0.0.0'
PORT = '5000'


@app.route('/states_list', strict_slashes=False)
def states_list():
    '''
    list of states
    '''
    template = '7-states_list.html'
    return render_template(template, states=storage.all(State))


if __name__ == '__main__':
    app.run(host=HOST, port=PORT)
