import json
from flask import Blueprint, render_template, request, redirect
from . import models

bp_facts = Blueprint("facts", __name__, url_prefix="/facts")


@bp_facts.route("/", methods=["POST"])
def index():
    if request.method == "POST":
        #print(request.form)
        submitter = request.form['submitter']
        fact = request.form["fact"]

        new_fact = models.db.facts(submitter, new_fact = fact)
        models.db.session.add(new_fact)
        models.db.session.commit()
        return redirect('/')
    
    rows = models.Fact.query.all()
    return render_template("facts/index.html", fact = rows)


@bp_facts.route("/new")
def facts_new():
    return render_template("new_facts.html")