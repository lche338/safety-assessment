#forms.py
#import the forms library
from flask_wtf import FlaskForm
from wtforms import (StringField,BooleanField,DateTimeField,
                    RadioField,SelectField,TextField,TextAreaField,
                    SubmitField, PasswordField)
from wtforms.ext.sqlalchemy.fields import QuerySelectField
#import the  validators that will be required to build the application
from wtforms.validators import DataRequired, EqualTo
from wtforms import ValidationError

class SafetyQuestionnaireForm(FlaskForm):
    #create the forms details
    kid_name = StringField('Please enter your name.',validators=[DataRequired()]
                           
    grandparent_name = StringField('Please enter your grandparent name.',validators=[DataRequired()])

    grandparent_gender = SelectField('Selet the gender of your grandparent:',
                    choices =[('Male','Male'),('Female','Female')],validators=[DataRequired()])
                           
    grandparent_age = SelectField('Selet the age of your grandparents:',
                    choices =[('65-74','65-74'),('75-84','75-84'),('85-94','85-94'),('95+','95+'),('none of above or not sure','none of above or not sure')],validators=[DataRequired()])

    adequate_light = SelectField('Does the house where your grandparent lived have adequate lighting in the following areas? (mutiple choice)',
                        choices=[('Bedroom','Bedroom'),('Kitchen','Kitchen'),('Living Room','Living Room'),('Walkways','Walkways'),('Laundry','Laundry'),('Bathroom','Bathroom'),('Stairs','Stairs'),('Driveway and garage','Driveway and garage')], validators=[DataRequired()])

    night_light = SelectField('Does the house where your grandparent lived have night-lights or signs giving directions to the following areas? (mutiple choice)',
                        choices=[('Bedroom','Bedroom'),('Kitchen','Kitchen'),('Living Room','Living Room'),('Walkways','Walkways'),('Laundry','Laundry'),('Bathroom','Bathroom'),('Stairs','Stairs'),('Driveway and garage','Driveway and garage')], validators=[DataRequired()])                      
                           
    clear_path = RadioField('Do you think there is a clear, unobstructed path through the room?',
                    choices =[('Yes','Yes'),('No','No')],validators=[DataRequired()])

    floors_condition = RadioField('Do you think there is wood floors slip resistant and carpets in good condition with non-slip backing (not frayed or turned up, no upturned corner that someone could trip over)?',
                        choices =[('Yes','Yes'),('No','No')],validators=[DataRequired()])

    difficluties_walking = RadioField('Do you think your grandparent have difficluties in walking by himself/herself?',
                    choices =[('Yes','Yes'),('No','No')],validators=[DataRequired()])

    non_slip = RadioField('Do you think there is non-slip/non-skid floor surface even when wet in the Bathroom and Laundry?',
                        choices =[('Yes','Yes'),('No','No')],validators=[DataRequired()])

    grab_bars = RadioField('Ask your grandparent are there grab bars in the Bathroom as he/she needed?',
                        choices =[('Yes','Yes'),('No','No')],validators=[DataRequired()])

    telephone_reach = RadioField('Is there a telephone within reach of the bed? Are telephones positioned low enough so they can be reached if a fall occurs?',
                    choices =[('Yes','Yes'),('No','No')],validators=[DataRequired()])

    difficulties_chairs = RadioField('Do you think your grandparent have difficulties in getting up from chairs?',
                        choices =[('Yes','Yes'),('No','No')],validators=[DataRequired()])

    items_reached = RadioField('Do you think your grandparent used items visible and easily reached in the Kitchen?',
                    choices =[('Yes','Yes'),('No','No')],validators=[DataRequired()])

    handrails_needed = RadioField('Do you think there are handrails for stairs and steps in the house as needed for your grandparent?',
                    choices =[('Yes','Yes'),('No','No')],validators=[DataRequired()])

    smoke_detectors = RadioField('Are smoke detectors installed and working on every level of the home, outside sleeping areas and inside bedrooms?',
                    choices =[('Yes','Yes'),('No','No')],validators=[DataRequired()])

    fire_extinguisher = RadioField('Is there a fire extinguisher in the kitchen? and not expire?',
                    choices =[('Yes','Yes'),('No','No')],validators=[DataRequired()])
                           
    contact_information = RadioField('Ask your grandparent if he/she has contact information to someone in an emergency? If yes, Check if emergency numbers posted on or near all telephones?',
                    choices =[('Yes','Yes'),('No','No')],validators=[DataRequired()])
                           
    key_entry = RadioField('Is there a safe place outside to hide a key to the house for emergency entry?',
                    choices =[('Yes','Yes'),('No','No')],validators=[DataRequired()])
                           
    exit_plan = RadioField('Ask your grandparents if there is an emergency exit plan?',
                    choices =[('Yes','Yes'),('No','No')],validators=[DataRequired()])     

    submit = SubmitField('Submit Safety Assesment Questonnaire')

#form for deleting the data from the safety questionnaire table
class DeleteFromSafety(FlaskForm):
    submit = SubmitField('Clear all the data in the table')


#create a login form for the system administrator to login and perform CRUD operation son the database
class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Log In')

#add the registration form for the user
class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired(),EqualTo('pass_confirm', message='Passwords must match')])
    pass_confirm = PasswordField('Confirm Password', validators=[DataRequired()])
    submit = SubmitField('Register')

    def check_username(self,field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('Username already exists!')

class DisasterForm(FlaskForm):
    council_name = SelectField('Select Some Area',validators=[DataRequired()])
    submit = SubmitField('Submit')
