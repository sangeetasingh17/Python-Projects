from flask.app import Flask
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, EqualTo, Email, ValidationError
from market.models import User


class RegisterForm(FlaskForm):
    def validate_username(self , username_to_check):
        user = User.query.filter_by(username = username_to_check.data).first()

        if user:
            raise ValidationError('The username already exists!')
        
    def validate_email_address(self , email_address_to_check):
        email = User.query.filter_by(email_address = email_address_to_check.data).first()

        if email:
            raise ValidationError('email address already exists!')
#we have to prefix of the validate_ as the word we have usen in below..
#in this case we have usen username at below so we have written validate_username     ..... also validate_email_address follow the same rule.
            
    username = StringField(label='User Name', validators=[Length(min=6, max=30), DataRequired()])
    email_address = StringField(label='Email Address', validators=[
                                Email(), DataRequired()])
    password1 = PasswordField(label='Password', validators=[
                              Length(min=5), DataRequired()])
    password2 = PasswordField(label='Confirm Password', validators=[
                              EqualTo('password1'), DataRequired()])
    submit = SubmitField(label='Create an Account')

class LoginForm(FlaskForm):
    username = StringField(label='User Name', validators=[ DataRequired()])
    password = PasswordField(label='Password', validators=[ DataRequired()])
    submit = SubmitField(label='Log in to Account')



class PurchaseItemForm(FlaskForm):
    submit = SubmitField(label= "Purchase Item")


class SellItemForm(FlaskForm):
    submit = SubmitField(label= "sell Item")