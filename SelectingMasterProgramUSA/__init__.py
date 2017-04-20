from flask.ext.pymongo import PyMongo
from flask import Flask

app = Flask(__name__)
#app.config.from_object('config')
import SelectingMasterProgramUSA.views
import SelectingMasterProgramUSA.models
import SelectingMasterProgramUSA.forms