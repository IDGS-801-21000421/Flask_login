from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length

class LoginForm(FlaskForm):
    username = StringField('Usuario', validators=[DataRequired(), Length(min=3, message="Minimo 3 caracteres")])
    password = PasswordField('Contraseña', validators=[DataRequired()])
    submit = SubmitField('Iniciar sesión')

class RegisterForm(FlaskForm):
    username = StringField('Nuevo Usuario', validators=[DataRequired(), Length(min=3)])
    password = PasswordField('Nueva Contraseña', validators=[DataRequired(), Length(min=4)])
    submit = SubmitField('Registrar')