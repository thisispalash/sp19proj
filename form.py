from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, EqualTo, ValidationError
from model import User
 
class register_form(FlaskForm):
    name = StringField('Name: ', validators=[DataRequired(), Length(min=3,max=25)])
    username = StringField('Username: ', validators=[DataRequired(), Length(min=2, max=20)])
    submit= SubmitField('Join')

    def validate_username(self,username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('Username is taken! Please choose another one')

class login_form(FlaskForm):
    username= StringField('Username: ',validators=[DataRequired(),Length(min=2,max=20 )])
    password= PasswordField('Private Key: ',validators=[DataRequired()])
    remember= BooleanField('Remember me')
    submit=SubmitField('Enter')
