#!/usr/bin/env python

from flask import Flask
from pymongo import MongoClient

app = Flask(__name__)
#app.config.from_object('config')
client = MongoClient('localhost', 27017)
db = client.settings
all_data = db['MONGODB_DBNAME.Admissions']
import SelectingMasterProgramUSA.views
import SelectingMasterProgramUSA.models
import SelectingMasterProgramUSA.forms