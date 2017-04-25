from flask.views import MethodView
from flask import jsonify, request, abort
import pandas as pd
import openpyxl, xlrd
from data.rba.F16.FCMYJUN14D import compiledData

class rbaApi(MethodView):
    result = compiledData.to_json(orient='values',date_unit="s",date_format="epoch")
    
    def get(self):
        return jsonify({"data": self.result})