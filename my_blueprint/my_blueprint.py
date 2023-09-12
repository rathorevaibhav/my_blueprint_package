# my_blueprint.py
from flask import Blueprint

my_blueprint = Blueprint('my_blueprint', __name__)

@my_blueprint.route('/')
def index():
    return 'Hello from My Blueprint!'
