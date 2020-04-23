from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from flask_login import LoginManager
#import os

############################################

## SQL DATABASE SECTION ##
#date: April 10th 2020
#############################################
#setup the base dir for the database setup
#basedir = os.path.abspath(os.path.dirname(__file__))
#setup the database uri
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqllite:///' + os.path.join(basedir,'data.sqllite')
#turn off track modifications for the database
#app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#create a db instance
db = SQLAlchemy()
#migrate db with app
#Migrate(app,db)
#create the instance of login manager
login_manager = LoginManager()

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


##################################
### MODELS ######################
################################
#create the safety questionnaire model for the application that will be integrated with the front end

class safety_questionnaire_database(db.Model):
    #set of questionnaire: reference can be checked in safety questionnaire questions
    __tablename__ = 'safety_questionnaire'
    id = db.Column(db.Integer, primary_key = True)
    kid_name = db.Column(db.Text)
    grandparent_name = db.Column(db.Text)
    grandparent_gender = db.Column(db.Text)
    grandparent_age = db.Column(db.Text)
    adequate_sunlight = db.Column(db.Text)
    night_light = db.Column(db.Text)
    clear_path = db.Column(db.Text)
    floors_condition = db.Column(db.Text)
    difficluties_walking = db.Column(db.Text)
    non_slip = db.Column(db.Text)
    grab_bars = db.Column(db.Text)
    telephone_reach = db.Column(db.Text)
    difficulties_chairs = db.Column(db.Text)
    items_reached = db.Column(db.Text)
    handrails_needed = db.Column(db.Text)
    smoke_detectors = db.Column(db.Text)
    fire_extinguisher = db.Column(db.Text)
    contact_information = db.Column(db.Text)
    key_entry = db.Column(db.Text)
    exit_plan = db.Column(db.Text)
    
    #instantiate the values that are eing put up on the forms from the front end in the init method
    #the class
    def __init__(self,kid_name,grandparent_name,grandparent_gender,grandparent_age,adequate_sunlight,night_light,
    clear_path,floors_condition,difficluties_walking,non_slip,grab_bars,telephone_reach,difficulties_chairs,items_reached,
    handrails_needed,smoke_detectors,fire_extinguisher,contact_information,key_entry,exit_plan):
        self.kid_name = kid_name
        self.grandparent_name = grandparent_name
        self.grandparent_gender = grandparent_gender
        self.grandparent_age = grandparent_age
        self.adequate_sunlight = adequate_sunlight
        self.night_light = night_light
        self.clear_path = clear_path
        self.floors_condition = floors_condition
        self.difficluties_walking = difficluties_walking
        self.non_slip = non_slip
        self.grab_bars = grab_bars
        self.telephone_reach = telephone_reach
        self.difficulties_chairs = difficulties_chairs
        self.items_reached = items_reached
        self.handrails_needed = handrails_needed
        self.smoke_detectors = smoke_detectors
        self.fire_extinguisher = fire_extinguisher
        self.contact_information = contact_information
        self.key_entry = key_entry
        self.exit_plan = exit_plan

    #method to return the values
    # def __repr__(self):
    #     #print("This is called")
    #     #print(f'{ self.kid_name }')
    #     return f'{self.kid_name}'
########################################################################################################
#create the user table here for validating the system administrator
class User(db.Model, UserMixin):

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(64),unique=True, index = True)
    password_hash = db.Column(db.String(128))

    #create the instance of the db object
    def __init__(self,username, password):
        self.username = username
        self.password_hash = generate_password_hash(password)

    def check_password(self,password):
        return check_password_hash(self.password_hash, password)

########################################################################################################
class CouncilDisasterData(db.Model):
    __tablename__ = 'CouncilDisasterData'
    id = db.Column(db.Integer, primary_key = True)
    council = db.Column(db.Text)
    state = db.Column(db.Text)
    calamity_1 = db.Column(db.Text)
    calamity_2 = db.Column(db.Text)
    calamity_3 = db.Column(db.Text)
    calamity_4 = db.Column(db.Text)

    def __init__(self,council,state,calamity_1,calamity_2,calamity_3,calamity_4):
        self.council = council
        self.state = state
        self.calamity_1 = calamity_1
        self.calamity_2 = calamity_2
        self.calamity_3 = calamity_3
        self.calamity_4 = calamity_4
