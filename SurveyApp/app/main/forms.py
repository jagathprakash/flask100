from flask.ext.wtf import FlaskForm
from wtforms import RadioField, TextAreaField, SubmitField, TextField
from wtforms.validators import DataRequired, Optional


USER = "Slack Handle"

PURPOSE = "To Determine uniqueness of your vote"

QUESTION1 = "1. Do you find the public archives useful?"

QUESTION2 = "2. Do you find the public archives objectionable (as they expose your private conversation publicly) ?"

QUESTION3 = ("3. If you find them useful, but empathize with students who are concerned about privacy, "
             "are you okay with temporarily disabling archiving and switching to a private (student-created) "
             "alternative with access restricted to Georgia Tech students, alumni, instructors etcetera?")

QUESTION4 = ("4. Would you be happy to migrate the slack community to a compatible, very similar, free alternative"
             "with free unlimited history archiving included?")

QUESTION5 = "5. Any other thoughts on the archive policy?"


class SurveyForm(FlaskForm):
    user = TextField(USER, description=PURPOSE, validators=[DataRequired()])
    choice1 = RadioField(QUESTION1, choices=[("1", "Yes"), ("0", "No")], validators=[DataRequired()])
    choice2 = RadioField(QUESTION2, choices=[("1", "Yes"), ("0", "No")], validators=[DataRequired()])
    choice3 = RadioField(QUESTION3, choices=[("1", "Yes"), ("0", "No")], validators=[DataRequired()])
    choice4 = RadioField(QUESTION4, choices=[("1", "Yes"), ("0", "No")], validators=[DataRequired()])
    general = TextAreaField(QUESTION5, validators=[Optional()])
    submit = SubmitField("Submit")
