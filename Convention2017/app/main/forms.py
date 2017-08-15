from flask.ext.wtf import FlaskForm
from wtforms import SubmitField, StringField, SelectField
from wtforms.validators import DataRequired


class RegistrationForm(FlaskForm):
    firstName = StringField("Nau")
    lastName = StringField("Gher Nau")
    email = StringField("Email",
                        description="Email address to be associated with the Registration.",
                        validators=[DataRequired()])

    fields = [(str(num), str(num)) for num in range(0, 31)]

    regular = SelectField("Regular Entry: $20.00",
                          description="Regular Ticket",
                          choices=fields)

    free = SelectField("Children/Visitors: $0.00",
                       description="For Children below 10 or visiting relatives from India",
                       choices=fields)

    submit = SubmitField("Ami Averyo! (Proceed)")


class MembersForm(FlaskForm):
    pass

