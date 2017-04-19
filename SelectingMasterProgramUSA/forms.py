from wtforms import Form, BooleanField, StringField, PasswordField, validators
from wtforms.validators import DataRequired

class QueryForm(Form):
    school_name = StringField('Enter the UNIVERSITY NAME',validators = [DataRequired()])
    apply_major = StringField('Enter the MAJOR you want apply (in abbreviation)', validators = [DataRequired()])
