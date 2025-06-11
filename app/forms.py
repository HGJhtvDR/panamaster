from flask_wtf import FlaskForm
from wtforms import BooleanField, PasswordField, StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, Length


class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Пароль", validators=[DataRequired()])
    remember = BooleanField("Запомнить меня")


class RegistrationForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Пароль', validators=[DataRequired(), Length(min=6)])
    password2 = PasswordField('Повторите пароль', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Зарегистрироваться')


class ContactForm(FlaskForm):
    name = StringField("Ваше имя", validators=[DataRequired(), Length(min=2, max=50)])
    email = StringField("Email", validators=[DataRequired(), Email()])
    subject = StringField("Тема", validators=[DataRequired(), Length(min=2, max=100)])
    message = TextAreaField(
        "Сообщение", validators=[DataRequired(), Length(min=10, max=1000)]
    )
