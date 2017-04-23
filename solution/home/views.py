from flask import Blueprint, session, render_template

from bokeh.plotting import figure
from bokeh.io import output_file, show
from bokeh.embed import components
from bokeh.resources import CDN

home_app = Blueprint('home_app', __name__)

@home_app.route('/')
def home():
    
    x = [1,2,3,4,5]
    y = [6,7,8,9,10]
    f = figure()
    f.line(x,y)
    js,div = components(f)
    
    cdn_js = CDN.js_files[0]
    cdn_css = CDN.css_files[0]
    
    return render_template('home/home.html', js=js, div=div, cdn_js=cdn_js, cdn_css=cdn_css)