from flask_wtf import FlaskForm
from wtforms import TextAreaField, RadioField, StringField, SubmitField
from wtforms.validators import DataRequired

class SubmissionForm(FlaskForm):
    text = TextAreaField('Text', validators=[DataRequired()])
    radio = RadioField('Options', choices=[('wc','Word Count'),('cc','Character Count'),('fc','Most Frequent 5 Words')], default='wc')
    delimiters = StringField('Delimiters')
    submit = SubmitField('Submit Entry')