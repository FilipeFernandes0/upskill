from flask import Blueprint

ex_blueprint = Blueprint('blueprint',__name__)

@ex_blueprint.route('/')
def index():
    return 'Isto é uma aplicacao'