from flask import Blueprint, render_template

my_blueprint = Blueprint('my_blueprint', __name__, static_folder='static', template_folder='templates')

@my_blueprint.route('/')
def index():
    return 'Hello from My Blueprint!'

@my_blueprint.route('/show-template')
def show_template():
    return render_template('my_template.html', message='This is a template message.')
