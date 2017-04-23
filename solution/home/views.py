from flask import Blueprint, session, render_template

import pandas as pd
import openpyxl, xlrd

from bokeh.plotting import figure
from bokeh.io import output_file, show
from bokeh.embed import components
from bokeh.resources import CDN

home_app = Blueprint('home_app', __name__)

@home_app.route('/')
def home():
    
    # x = [1,2,3,4,5]
    # y = [6,7,8,9,10]
    
    data1 = pd.read_excel("http://www.rba.gov.au/statistics/tables/xls-hist/f16hist-2009-2015.xls")[[0, 8]]
    data1 = data1.iloc[10:]
    data1.columns = ["Date", "FCMYJUN14D"]
    data2 = pd.read_excel("http://www.rba.gov.au/statistics/tables/xls-hist/f16hist-2009-2015.xls", sheetname = 1)[[0,2]]
    data2 = data2.iloc[10:]
    data2.columns = ["Date", "FCMYJUN14D"]
    
    #join dataframes from 2 excel sheets and drop rows with null values
    frames = [data1, data2]
    result = pd.concat(frames).dropna()
    x=result["Date"]
    y=result["FCMYJUN14D"]
    
    f = figure()
    f.line(x,y)
    js,div = components(f)
    
    cdn_js = CDN.js_files[0]
    cdn_css = CDN.css_files[0]
    
    return render_template('home/home.html', js=js, div=div, cdn_js=cdn_js, cdn_css=cdn_css)