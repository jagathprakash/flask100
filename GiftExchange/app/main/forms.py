from flask.ext.wtf import FlaskForm
from wtforms import TextAreaField, SubmitField, StringField
from wtforms.validators import DataRequired


class ParticipantForm(FlaskForm):
    name = StringField("Name", description="Description", validators=[DataRequired()])
    email = StringField("Email", description="Description", validators=[DataRequired()])
    address = TextAreaField("Address", description="Description", validators=[DataRequired()])
    gifts = TextAreaField("Address", description="Description", validators=[DataRequired()])
    charity = TextAreaField("Address", description="Description", validators=[DataRequired()])
    submit = SubmitField("Submit")
