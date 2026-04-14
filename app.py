"""Car Trust — second-hand purchase verification (mock APIs)."""

from __future__ import annotations

import os

from flask import Flask, redirect, render_template, request, url_for

from field_config import FIELDS, SOURCE_LABELS
from matching import build_rows, overall_summary
from mock_apis import (
    SCENARIO_CHOICES,
    call_insurance_api,
    call_rto_api,
    call_third_party_api,
)

app = Flask(__name__)
app.config["SECRET_KEY"] = "car-trust-dev-key"


def _fields_by_source():
    out = {"rto": [], "insurance": [], "third_party": []}
    for f in FIELDS:
        out[f.source].append(f)
    return out


@app.get("/")
def index():
    return render_template("login.html")


@app.post("/login")
def login():
    name = (request.form.get("name") or "").strip()
    email = (request.form.get("email") or "").strip()
    phone = (request.form.get("phone") or "").strip()

    if not (name and email and phone):
        return render_template(
            "login.html",
            error="Please fill Name, Email ID, and Phone Number to continue.",
            values={"name": name, "email": email, "phone": phone},
        )

    return redirect(url_for("home"))


@app.get("/home")
def home():
    return render_template("home.html")


@app.get("/details")
def details():
    grouped_fields = _fields_by_source()
    return render_template(
        "index.html",
        fields=FIELDS,
        grouped_fields=grouped_fields,
        scenarios=SCENARIO_CHOICES,
        source_labels=SOURCE_LABELS,
    )


@app.post("/verify")
def verify():
    scenario = request.form.get("scenario") or SCENARIO_CHOICES[0][0]
    user_values = {f.key: (request.form.get(f.key) or "").strip() for f in FIELDS}

    rto = call_rto_api(scenario)
    insurance = call_insurance_api(scenario)
    third_party = call_third_party_api(scenario)

    rows = build_rows(user_values, rto, insurance, third_party)
    summary = overall_summary(rows)

    # Group rows for template
    grouped = {"rto": [], "insurance": [], "third_party": []}
    for row in rows:
        grouped[row["source"]].append(row)

    raw_responses = {"rto": rto, "insurance": insurance, "third_party": third_party}

    return render_template(
        "results.html",
        fields=FIELDS,
        rows=rows,
        grouped=grouped,
        summary=summary,
        scenario=scenario,
        source_labels=SOURCE_LABELS,
        raw_responses=raw_responses,
    )


@app.get("/results")
def results_redirect():
    return redirect(url_for("details"))


if __name__ == "__main__":
    host = os.environ.get("FLASK_RUN_HOST", "0.0.0.0")
    port = int(os.environ.get("PORT", 3000))
    debug = os.environ.get("FLASK_DEBUG", "false").lower() == "true"
    app.run(host=host, port=port, debug=debug)
