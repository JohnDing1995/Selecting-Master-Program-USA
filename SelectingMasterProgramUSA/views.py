from flask import request
from SelectingMasterProgramUSA import app, client
from SelectingMasterProgramUSA.models import Admission
import jinja2
import pprint
from flask import render_template
from pymongo import MongoClient

@app.route('/',methods=['POST','GET'])
def query_university():
    if request.method == "POST":
        #client = MongoClient('localhost', 27017)
        db = client.settings
        all_data = db['MONGODB_DBNAME.Admissions']
        school_name = request.form['name']
        major = request.form['major']
        result = all_data.find({'admission_school': school_name, 'major': major})
        for ad in result:
            pprint.pprint(ad)
    return render_template('main.html')


