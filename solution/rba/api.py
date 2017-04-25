from flask.views import MethodView
from flask import jsonify, request, abort
import pandas as pd
import openpyxl, xlrd

class rbaApi(MethodView):
    #download excel file from rba.gov.au, remove unwanted rows and columns
    data1 = pd.read_excel("http://www.rba.gov.au/statistics/tables/xls-hist/f16hist-2009-2015.xls")[[0, 8]]
    data1 = data1.iloc[10:]
    data1.columns = ["Date", "FCMYJUN14D"]
    data2 = pd.read_excel("http://www.rba.gov.au/statistics/tables/xls-hist/f16hist-2009-2015.xls", sheetname = 1)[[0,2]]
    data2 = data2.iloc[10:]
    data2.columns = ["Date", "FCMYJUN14D"]
    
    #join dataframes from 2 excel sheets and drop rows with null values
    frames = [data1, data2]
    result = pd.concat(frames).dropna().to_json(orient='values',date_unit="s",date_format="epoch")
    
    def get(self):
        return jsonify({"data": self.result})