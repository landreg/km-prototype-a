from flask.ext.wtf import Form
from wtforms import StringField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class searchForm(Form):
    #subjectArea   = StringField('openid', validators=[DataRequired()])
    #searchKeyWord = StringField('openid', validators=[DataRequired()])
    #remember_me = BooleanField('remember_me', default=False)
    searchString = StringField("Search String")
    submit = SubmitField("Search")
