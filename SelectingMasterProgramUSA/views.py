from flask import request

from SelectingMasterProgramUSA import app
import jinja2
from flask import render_template

@app.route('/',methods=['GET','POST'])
def query_university():
    if request.method == 'POST':
        school_name = request.form['name']
        major = request.form['major']

    return render_template('main.html')

