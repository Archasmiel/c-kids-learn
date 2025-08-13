from flask_wtf import FlaskForm
from wtforms import PasswordField, SubmitField
from wtforms.validators import DataRequired, EqualTo, Length

class ChangePasswordForm(FlaskForm):
    current_password = PasswordField("Поточний пароль", validators=[DataRequired()])
    new_password = PasswordField("Новий пароль", validators=[DataRequired(), Length(min=6)])
    confirm_password = PasswordField("Підтвердіть пароль", validators=[
        DataRequired(),
        EqualTo("new_password", message="Паролі не співпадають.")
    ])
    submit = SubmitField("Змінити пароль")
