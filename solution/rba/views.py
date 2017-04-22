from flask import Blueprint, session, render_template

from flask import Blueprint
from rba.api import rbaApi
rba_app = Blueprint('rba_app', __name__)

#return the jsonify labelled petsth
rba_app.add_url_rule('/rba/', view_func=rbaApi.as_view('rba'))