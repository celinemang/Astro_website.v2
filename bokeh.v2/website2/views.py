import dataclasses
from flask import Blueprint, render_template, request, flash, jsonify
from . import db
from flask_login import  login_required, current_user
import json


views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST': 
        note = request.form.get('note')#Gets the note from the HTML 

        if len(note) < 1:
            flash('Note is too short!', category='error') 
        else:
            new_note = Note(data=note, user_id=current_user.id)  #providing the schema for the note 
            db.session.add(new_note) #adding the note to the database 
            db.session.commit()
            flash('Note added!', category='success')

    return render_template("home.html", user=current_user)       


from pandas_datareader import data as pdr
import datetime
from bokeh.plotting import figure, show, output_file
from bokeh.embed import components
from bokeh.resources import CDN

@views.route('/plot/')
def plot():
    
    start=datetime.datetime(2015,11,1)
    end=datetime.datetime(2016,3,10)

    df = dataclasses.DataReader(name = "GOOG", data_source = "yahoo", start = start, end = end)

    def inc_dec(c,o):
        if c > o:
            value = "Increase"
        elif c < o:
            value = "Decrease"
        else:
            value = "Equal"
        return value

    df["Status"] = [inc_dec(c,o) for c, o in zip(df.Close, df.Open)]
    df["Middle"] = (df.Open+df.Close)/2
    df["Height"] = abs(df.Close-df.Open)

    p = figure(x_axis_type = 'datetime', width = 1000, height = 300, responsive= True)
    p.title = "Candlestick Chart"
    p.grid.grid_line_alpha = 0.3

    hours_12 = 12*60*60*1000

    p.segment(df.index, df.High, df.index, df.Low, color = "Black")
    p.rect(df.index[df.Status == "Increase"], df.Middle[df.Status == "Increase"],
        hours_12,df.Height[df.Status == "Increase"], fill_color = "#CCFFFF", line_color = "black")

    p.rect(df.index[df.Status == "Decrease"], df.Middle[df.Status == "Decrease"],
        hours_12,df.Height[df.Status == "Decrease"], fill_color = "#FF3333", line_color = "black")

    views, div1 = components(p)
    cdn_js = CDN.js_files[0]
    cdn_css = CDN.css_files[0]
    return render_template("plot.html", 
    views = views, 
    div1 = div1,
    cdn_js = cdn_js,
    cdn_css = cdn_css )





