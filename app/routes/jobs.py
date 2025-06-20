from typing import cast

from flask import Blueprint, flash, redirect, render_template, url_for
from sqlalchemy.exc import SQLAlchemyError

from app.models.job import Job

bp = Blueprint("jobs", __name__)


@bp.route("/jobs")
def index() -> str:
    """Show all job listings."""
    try:
        jobs = Job.query.all()
        return cast(str, render_template("jobs/index.html", jobs=jobs))
    except SQLAlchemyError:
        flash("Error loading jobs", "error")
        return cast(str, render_template("jobs/index.html", jobs=[]))


@bp.route("/jobs/<int:job_id>")
def show(job_id: int) -> str:
    """Show a specific job listing."""
    try:
        job = Job.query.get_or_404(job_id)
        return cast(str, render_template("jobs/show.html", job=job))
    except SQLAlchemyError:
        flash("Error loading job", "error")
        return cast(str, redirect(url_for("jobs.index")))


@bp.route("/jobs/apply/<int:job_id>")
def apply(job_id: int) -> str:
    """Apply for a job."""
    try:
        job = Job.query.get_or_404(job_id)
        return cast(str, render_template("jobs/apply.html", job=job))
    except SQLAlchemyError:
        flash("Error loading job", "error")
        return cast(str, redirect(url_for("jobs.index")))
