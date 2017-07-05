from flask import request
from SelectingMasterProgramUSA import app, client
from SelectingMasterProgramUSA.models import Admission
import jinja2
import pprint
from flask import render_template
from pymongo import MongoClient


@app.route('/', methods=['POST', 'GET'])
def query_university():
    school_name_and_major = " "
    query_result = ""
    if request.method == "POST":
        # client = MongoClient('localhost', 27017)
        db = client.settings
        all_data = db['MONGODB_DBNAME.Admissions']

        school_name_and_major = request.form['name_major']
        print(school_name_and_major)
        school_name = school_name_and_major.split(' ')[0]
        major = school_name_and_major.split(' ')[1]
        school_name_re = ".*" + school_name + ".*"
        major_re = ".*" + major + ".*"
        query_result = all_data.find({"admission_school":{'$regex':school_name_re,'$options':'$i'},
                                      "admission_major":{'$regex':major_re,'$options':'$i'}})
        # print(type(query_result))
        #for ad in query_result:
        #    pprint.pprint(ad)


        # for test only
    return render_template('main.html', query_result =query_result, school_name_and_major = school_name_and_major)

