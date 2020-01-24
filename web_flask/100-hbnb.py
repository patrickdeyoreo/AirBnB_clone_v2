#!/usr/bin/python3
'''
Start a Flask web application
'''
from models import storage
from models.amenity import Amenity
from models.place import Place
from models.state import State
from models.user import User
from flask import Flask, render_template
app = Flask(__name__)

HOST = '0.0.0.0'
PORT = '5000'


@app.route('/hbnb', strict_slashes=False)
def hbnb_filters():
    '''
    list states or show details of a particular state
    '''
    temp = '100-hbnb.html'
    amenities = storage.all(Amenity).values()
    states = storage.all(State).values()
    places = storage.all(Place).values()
    users = storage.all(User)
    users = {p.id: users['User.{}'.format(p.user_id)] for p in places}
    return render_template(
        temp, amenities=amenities, states=states, places=places, users=users
    )


@app.teardown_appcontext
def close_storage(exc):
    '''
    close storage
    '''
    storage.close()


if __name__ == '__main__':
    app.run(host=HOST, port=PORT)
