from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import InputRequired, Email, Length


class CreatePostForm(FlaskForm):
    title = StringField("title", validators=[InputRequired(), Length(max=50)])
    subtitle = StringField("subtitle", validators=[InputRequired(), Length(max=300)])
    content = StringField("content", validators=[InputRequired(), Length(max=1000)])


class LoginForm(FlaskForm):
    email = StringField("email", validators=[InputRequired()])
    password = PasswordField("password", validators=[InputRequired()])
    remember = BooleanField("remember me")


class RegisterForm(FlaskForm):
    email = StringField("email", validators=[InputRequired()])
    name = StringField("name", validators=[InputRequired()])
    password = PasswordField("password", validators=[InputRequired()])
