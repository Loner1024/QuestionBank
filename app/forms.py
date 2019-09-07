from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField, RadioField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()], render_kw={'placeholder': 'Username'})
    password = PasswordField('Password', validators=[DataRequired()], render_kw={'placeholder': 'Password'})
    submit = SubmitField('Login', render_kw={'class': 'ui fluid large teal submit button'})


class AnswerForm(FlaskForm):
    # answer_1 = RadioField(self.topic, choices=[('A', self.option_A), ('B', self.option_B), ('C', self.option_C), ('D', self.option_D)], validators=[DataRequired()])
    submit = SubmitField('Submit', render_kw={'class': 'ui fluid medium teal submit button'})

    def __init__(self, topic, option_A, option_B, option_C, option_D):
        self.option_A = option_A
        self.option_B = option_B
        self.option_C = option_C
        self.option_D = option_D
        self.topic = topic
