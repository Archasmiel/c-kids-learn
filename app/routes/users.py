from flask import Blueprint, redirect, url_for, flash, render_template
from flask_login import login_required, current_user
from sqlalchemy import func
from ..forms.update_profile import UpdateProfileForm
from ..models.teacher_request import TeacherRequest
from ..models.user import User
from ..services.database import db
from ..utils.decorators import teacher_required

bp = Blueprint("users", __name__)


@bp.route("/profile", methods=["GET"])
@login_required
def profile():
    form = UpdateProfileForm(username=current_user.username)
    return render_template("profile.html", form=form)


@bp.route("/profile", methods=["POST"])
@login_required
def update_profile():
    form = UpdateProfileForm()
    if not form.validate_on_submit():
        flash("Перевірте правильність даних.", "danger")
        return redirect(url_for("users.profile"))

    new_username_lc = (form.username.data or "").strip().lower()
    if not new_username_lc:
        flash("Ім'я користувача не може бути порожнім.", "danger")
        return redirect(url_for("users.profile"))

    # Uniqueness (case-insensitive), excluding current user
    exists = (
        db.session.query(User.id)
        .filter(func.lower(User.username) == new_username_lc, User.id != current_user.id)
        .first()
    )
    if exists:
        flash("Такий користувач вже існує.", "danger")
        return redirect(url_for("users.profile"))

    # Update
    current_user.username = new_username_lc
    db.session.commit()
    flash("Профіль оновлено.", "success")
    return redirect(url_for("users.profile"))


@bp.route("/request-teacher", methods=["POST"])
@login_required
def request_teacher():
    # Create or keep pending request
    req = TeacherRequest.query.filter_by(user_id=current_user.id).first()
    if req:
        if req.status == "pending":
            flash("Ваш запит уже очікує розгляду.", "info")
        elif req.status == "approved":
            flash("Вам вже надано роль викладача.", "success")
        else:  # rejected → allow re-request by resetting to pending
            req.status = "pending"
            db.session.commit()
            flash("Повторний запит надіслано.", "success")
        return redirect(url_for("users.profile"))

    # create new
    req = TeacherRequest(user_id=current_user.id, status="pending")
    db.session.add(req)
    db.session.commit()
    flash("Запит на роль викладача надіслано адміністратору.", "info")
    return redirect(url_for("users.profile"))


@bp.route("/dashboard", methods=["GET"])
@teacher_required
def dashboard():
    return render_template("dashboard.html")


@bp.route("/projects", methods=["GET", "POST"])
@login_required
def projects():
    return render_template("dashboard.html")
