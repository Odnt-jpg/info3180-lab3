from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email, Length

class Contact_Form(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(max=100)])
    email = StringField('Email', validators=[DataRequired(), Email(), Length(max=100)]) #checks specifically the email format 
    subject = StringField('Subject', validators=[DataRequired(), Length(max=150)])
    message = TextAreaField('Message', validators=[DataRequired(), Length(max=500)])
    submit = SubmitField('Send Message')
