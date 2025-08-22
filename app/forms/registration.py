from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, EqualTo


class RegistrationForm(FlaskForm):
    username = StringField('Нікнейм', validators=[DataRequired(), Length(min=3, max=80)])
    password = PasswordField('Пароль', validators=[DataRequired(), Length(min=6)])
    confirm_password = PasswordField('Пароль повторно', validators=[
        DataRequired(), EqualTo('password', message='Паролі не збігаються')
    ])
    submit = SubmitField('Зареєструватися')
