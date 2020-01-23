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
    STATES = storage.all(State).values()
    return render_template(TEMPLATE, states=STATES)


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    '''
    list cities by state
    '''
    TEMPLATE = '8-cities_by_states.html'
    STATES = storage.all(State).values()
    STATE_CITIES = {state.id: state.cities for state in STATES}
    return render_template(TEMPLATE, states=STATES, state_cities=STATE_CITIES)


if __name__ == '__main__':
    app.run(host=HOST, port=PORT)
