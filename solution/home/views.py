from flask import Blueprint, session, render_template

import pandas as pd
import openpyxl, xlrd

from bokeh.plotting import figure
from bokeh.io import output_file, show
from bokeh.embed import components
from bokeh.resources import CDN
from bokeh.models import HoverTool, ColumnDataSource

# from data.rba.F16.FCMYJUN14D import compiledData
from FCMYJUN14D import compiledData

home_app = Blueprint('home_app', __name__)

@home_app.route('/')
def home():
    x=compiledData["Date"]
    y=compiledData["FCMYJUN14D"]
    
    data=dict(
            date=[x.strftime("%d-%m-%Y") for x in compiledData['Date']],
            rate=compiledData['FCMYJUN14D']
        )
    
    #implement hover tooltip
    hover = HoverTool(
        tooltips=[
            ("(day,rate)", "(@date, $y %)")
        ]
    )
    
    f = figure(x_axis_type="datetime", tools="pan,wheel_zoom,box_zoom,reset", plot_width=1000)
    f.add_tools(hover)
    f.line(x,y, source = data)
    
    #format plot
    f.title.text="Effective Annual Yield Time Series"
    f.title.text_font="times"
    f.title.text_font_size="44px"
    f.title.align="center"
    
    f.xaxis.axis_label = "Year"
    f.yaxis.axis_label = "Semi annual yield %"
    
    #extract javascript and html from the figure to pass to view
    js,div = components(f)
    #get js and css using inbuilt cdn methods
    cdn_js = CDN.js_files[0]
    cdn_css = CDN.css_files[0]
    
    return render_template('home/home.html', js=js, div=div, cdn_js=cdn_js, cdn_css=cdn_css)