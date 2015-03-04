from flask.ext.wtf import Form
from wtforms import StringField, BooleanField, SubmitField, SelectField
from wtforms.validators import DataRequired

class searchForm(Form):
    searchArea = SelectField('Search Area', choices=[('all', 'All'), ('reg', 'Registration'), ('info', 'Information Services'), ('cust', 'Customer Handling')])
    searchString = StringField("Search String")
    submit = SubmitField("Search")
