from flask import render_template
from .forms import SurveyForm
from ..models import db_session
from . import main

from sqlalchemy import text


def insert_survey_result(slack, choice1, choice2, choice3, choice4, general):
    s = text("INSERT INTO SurveyResults VALUES (NULL, :slack, :choice1, :choice2, :choice3, :choice4, :general)").bindparams(
        slack=slack,
        choice1=choice1,
        choice2=choice2,
        choice3=choice3,
        choice4=choice4,
        general=general)
    result = db_session.execute(s)
    result.close()
    db_session.commit()


@main.route("/", methods=['GET', 'POST'])
def login():
    survey_form = SurveyForm()
    if survey_form.validate_on_submit():
        slack = survey_form.user.data
        choice1 = int(survey_form.choice1.data)
        choice2 = int(survey_form.choice2.data)
        choice3 = int(survey_form.choice3.data)
        choice4 = int(survey_form.choice4.data)
        general = survey_form.general.data

        insert_survey_result(slack, choice1, choice2, choice3, choice4, general)
        return render_template("thanks.html")

    return render_template("survey.html", form=survey_form)
