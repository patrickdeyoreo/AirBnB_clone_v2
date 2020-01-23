#!/usr/bin/python3
'''
Start a Flask web application
'''
from models import storage
from models.amenity import Amenity
from models.place import place
from models.state import State
from flask import Flask, render_template
app = Flask(__name__)

HOST = '0.0.0.0'
PORT = '5000'


@app.route('/hbnb', strict_slashes=False)
def hbnb_filters():
    '''
    list states or show details of a particular state
    '''
    template = '100-hbnb.html'
    kwargs = {
        'amenities': storage.all(Amenity).values(),
        'places': storage.all(Place).values(),
        'states': storage.all(State).values(),
    }
    return render_template(template, **kwargs)


@app.teardown_appcontext
def close_storage(exc):
    '''
    close storage
    '''
    storage.close()


if __name__ == '__main__':
    app.run(host=HOST, port=PORT)
