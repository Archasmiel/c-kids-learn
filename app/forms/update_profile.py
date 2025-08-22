from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length


class UpdateProfileForm(FlaskForm):
    username = StringField("Ім'я користувача", validators=[DataRequired(), Length(min=3, max=80)])
    submit = SubmitField("Зберегти")
