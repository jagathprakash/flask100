from flask import redirect
from flask import render_template
from flask import url_for

from .forms import ParticipantForm
from ..models import db_session
from . import main

from sqlalchemy import text


def insert_survey_result(name, email, address, gifts, charity):
    s = text("INSERT INTO Participants VALUES (:name, :email, :address, :gifts, :charity)").bindparams(
        name=name,
        email=email,
        address=address,
        gifts=gifts,
        charity=charity)
    result = db_session.execute(s)
    result.close()
    db_session.commit()


@main.route("/thanks", methods=['GET'])
def thanks():
    return render_template("thanks.html")



@main.route("/", methods=['GET', 'POST'])
def login():
    participant = ParticipantForm()
    if participant.validate_on_submit():
        name = participant.name.data
        email = participant.email.data
        address = participant.address.data
        gifts = participant.gifts.data
        charity = participant.charity.data
        insert_survey_result(name, email, address, gifts, charity)
        return redirect(url_for("main.thanks"))

    return render_template("participant.html", form=participant)
