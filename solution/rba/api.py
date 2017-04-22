from flask.views import MethodView
from flask import jsonify, request, abort
import pandas as pd

class rbaApi(MethodView):
    # data = [
    #     {"id": 1, "name": u"Rob"},
    #     {"id": 2, "name": u"Jim"},
    #     {"id": 3, "name": u"Rambo"}
    #     ]
    data = pd.read_excel("http://www.rba.gov.au/statistics/tables/xls-hist/f16hist-2009-2015.xls").to_json()
        
    def get(self):
        return jsonify({"data": self.data})