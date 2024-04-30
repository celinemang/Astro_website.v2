# Pip install waitress

from flask import Flask, render_template, request, make_response
#from waitress import serve
# from flask_mysqldb import MySQL
from pandas_datareader import data 
from bokeh.plotting import figure, show, output_file
from bokeh.embed import components
from bokeh.resources import CDN
# 


app = Flask(__name__)
app.url_map.strict_slashes = False
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

# app.config['MYSQL_HOST'] = 'localhost'
# app.config['MYSQL_USER'] = 'root'
# app.config['MYSQL_PASSWORD'] = 'root'
# app.config['MYSQL_DB'] = 'Students'

# mysql = MySQL(app)

@app.route("/")
@app.route('/home', methods=['GET', 'POST'])

def home():
    title = 'Home'
    p = figure(title="Simple line example", x_axis_label='x', y_axis_label='y', width=450, height=450)

    p.line([1, 2, 3, 4, 5], [6, 7, 2, 4, 5], legend_label="Temp.", line_width=2)
    
    # Generate JS and DIV components
    script, div = components(p)

    # Render template with components
    return render_template('index.html', script=script, div=div, cdn_js=CDN.js_files[0])





@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        userdetails = request.form
        fname = userdetails['fname']
        # cur = mysql.connection.cursor()
        # cur.execute("INSERT INTO student(idnum,name) VALUES(%i,%s)",(54252,'Testing1'))
        # mysql.connection.commit()
        # cur.close()
        # return "{name}"
    return render_template('contact.html')

import dataclasses
from pandas_datareader import data as pdr
import datetime
from bokeh.plotting import figure, show, output_file
from bokeh.embed import components
from bokeh.resources import CDN



if __name__ == '__main__':
    #serve(app, host="0.0.0.0", port=8080)
    app.run(debug=True)