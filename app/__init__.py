from flask import blueprints

api = blueprints.Blueprint('api', __name__)

from . import routes