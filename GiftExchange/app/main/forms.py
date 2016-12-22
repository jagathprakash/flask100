from flask.ext.wtf import FlaskForm
from wtforms import TextAreaField, SubmitField, StringField
from wtforms.validators import DataRequired


class ParticipantForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired()])
    address = TextAreaField("Address", description="Address to ship (physical gifts):", validators=[DataRequired()])
    gifts = TextAreaField("Gifts you like:", description="Gifts that you prefer to get.", validators=[DataRequired()])
    charity = TextAreaField("Charities you like:", description="Charity that you prefer to support.", validators=[DataRequired()])
    submit = SubmitField("Make a Wish!")
