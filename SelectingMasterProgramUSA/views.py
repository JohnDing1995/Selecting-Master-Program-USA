from flask import request
from SelectingMasterProgramUSA import app, all_data
from SelectingMasterProgramUSA.models import Admission
import jinja2
import pprint
from flask import render_template

@app.route('/', methods=['GET'])
def main_page():
    return render_template('main.html')

@app.route('/',methods=['POST'])
def query_university():
    school_name = request.form['name']
    major = request.form['major']
    result = all_data.find({'admission_school': school_name, 'major': major})
    for ad in result:
        pprint.pprint(ad)



