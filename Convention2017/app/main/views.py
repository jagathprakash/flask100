from flask import redirect
from flask import render_template
from flask import url_for
from wtforms import StringField, SubmitField, Label, Field, RadioField, SelectField, TextField
from wtforms.validators import DataRequired

from .forms import RegistrationForm, MembersForm
from ..models import db_session
from . import main

from sqlalchemy import text


@main.route("/thanks", methods=['GET'])
def thanks():
    return render_template("thanks.html")


def insert_registration_record(email, FirstName, FamilyName, cost, donation, paid, Address, State):
    s = text("INSERT INTO Registration VALUES (:email, :FirstName, :FamilyName, :cost, :donation, :paid, :Address, "
             ":State)").bindparams(
            email=email,
            FirstName=FirstName,
            FamilyName=FamilyName,
            cost=cost,
            donation=donation,
            paid=paid,
            Address=Address,
            State=State)

    result = db_session.execute(s)
    result.close()
    db_session.commit()


def insert_members_record(email, MemberFName, MemberLName):
    s = text("INSERT INTO Members VALUES (:RegistrationEmail, :MemberFName, :MemberLName)").bindparams(
            RegistrationEmail=email,
            MemberFName=MemberFName,
            MemberLName=MemberLName)

    result = db_session.execute(s)
    result.close()
    db_session.commit()


@main.route("/", methods=['GET', 'POST'])
def login():
    registrationForm = RegistrationForm()

    if registrationForm.validate_on_submit():
        email = registrationForm.email.data
        regular = registrationForm.regular.data
        free = registrationForm.free.data

        # insert_registration_record(email, FirstName, FamilyName, cost, donation, paid, Address, State)
        return redirect(url_for("main.add_members", username=email, regular=regular, free=free))

    return render_template("registration.html", form=registrationForm)


@main.route("/addmembers/<username>/<regular>/<free>", methods=['GET', 'POST'])
def add_members(username, regular, free):
    membersForm = MembersForm()

    class AddMembers(MembersForm):
        pass

    for regular_user in range(1, int(regular) + 1):
        setattr(AddMembers, "RFName" + str(regular_user), StringField("Attendee " + str(regular_user) + " Nau",
                                                                      validators=[DataRequired()]))

    for free_user in range(1, int(free) + 1):
        setattr(AddMembers, "FFName" + str(free_user), StringField("Child / Visitor " + str(free_user) + " Nau",
                                                                   validators=[DataRequired()]))

    AddMembers.choice1 = SelectField('Accommodation',
                                    description="Would you need accomodation when travelling to Bay Area ?",
                                    choices=[('no','No'), ('yes', 'Yes')])

    AddMembers.choice2 = SelectField("Tour",
                                    description="Would you like to join local site seeing tour?",
                                    choices=[('no','No'), ('yes', 'Yes')])

    AddMembers.donate = StringField("Donation", description="Event of this scale is made possible only by generous "
                                                            "donations. The registration cost is only nominal. "
                                                            "If you like to donate, please enter your donation amount.",
                                    default=0.0)

    AddMembers.submit = SubmitField("Proceed to Payment.")

    addmembers_instance = AddMembers()

    if membersForm.validate_on_submit():
        return redirect(url_for("main.payment",
                                username=username, cost=int(regular) * 20, donation=float(addmembers_instance.donate.data)))

    return render_template("members.html", form=addmembers_instance)


@main.route("/payment/<username>/<cost>/<donation>", methods=['GET', 'POST'])
def payment(username, cost, donation):
    return render_template("payment.html",
                           cost = "Cost: $" + str(cost),
                           donation = "Donation: $" + str(donation),
                           total = "Total: $" + str(int(cost) + float(donation)))
