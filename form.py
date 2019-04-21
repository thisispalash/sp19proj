from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, EqualTo, ValidationError
from model import User
 
class register_form(FlaskForm):
    username = StringField('Username: ',validators=[DataRequired(), Length(min=2, max=20)])
    password= PasswordField('Password: ',validators=[ DataRequired()])
    confirm_password= PasswordField('Confirm Password: ',validators=[ DataRequired(),EqualTo('password')])
    submit= SubmitField('Sign up') 

    def validate_username(self,username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('Username is taken! Please choose another one')

class login_form(FlaskForm):
    username= StringField('Username: ',validators=[DataRequired(),Length(min=2,max=20 )])
    password= PasswordField('Password: ',validators=[DataRequired()])
    remember= BooleanField('Remember me')
    submit=SubmitField('Log in')
