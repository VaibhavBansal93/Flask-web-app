from flask_wtf import FlaskForm
# to declare that the field will contains string data 
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo

 #use validators to validate the imput
    #make sure that the username field is not left blank
    #by the user and also to restrict the size of input

class RegistrationForm(FlaskForm):
    username = StringField('Username',validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',validators = [ DataRequired(), Email() ] )
    password = PasswordField('Password',validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',validators=[DataRequired(),EqualTo('password')] )
    submit = SubmitField('Sign Up')

class LoginForm(FlaskForm):
    email = StringField('Email',validators = [ DataRequired(), Email() ] )
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',validators=[DataRequired(),EqualTo('password')] )
    remember = BooleanField('Remember me')
    submit = SubmitField('Login')