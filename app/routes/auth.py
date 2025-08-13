from flask import Blueprint, flash, redirect, url_for, render_template, request
from flask_login import current_user, login_required, login_user, logout_user
from ..forms.registration import RegistrationForm
from ..forms.login import LoginForm
from ..forms.change_password import ChangePasswordForm
from ..models.user import User
from ..services.database import db
from sqlalchemy import func
from sqlalchemy.exc import IntegrityError

bp = Blueprint('auth', __name__)



def _norm_username(s: str) -> str:
    return (s or "").strip().lower()


@bp.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('basic.index'))

    form = RegistrationForm()
    if form.validate_on_submit():
        username_lc = _norm_username(form.username.data)

        exists = (
            db.session.query(User.id)
            .filter(func.lower(User.username) == username_lc)
            .first()
        )

        if exists:
            flash('Такий нікнейм зайнято', 'danger')
        else:
            try:
                user = User(username=username_lc)
                user.set_password(form.password.data)
                db.session.add(user)
                db.session.commit()
                flash('Зареєстровано успішно. Можна увійти..', 'success')
                return redirect(url_for('auth.login'))
            except IntegrityError:
                db.session.rollback()
                flash('Такий нікнейм зайнято', 'danger')

    return render_template('register.html', form=form)


@bp.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('basic.index'))

    form = LoginForm()
    if form.validate_on_submit():
        username_lc = _norm_username(form.username.data)

        user = (
            db.session.query(User)
            .filter(func.lower(User.username) == username_lc)
            .first()
        )

        if user and user.check_password(form.password.data):
            login_user(user, remember=getattr(form, "remember", None) and form.remember.data)

            next_url = request.args.get('next')
            if not next_url or '://' in next_url or next_url.startswith('//'):
                next_url = url_for('basic.index')

            flash('Успішний вхід :)', 'success')
            return redirect(next_url)

        flash('Нікнейм або пароль неправильний.', 'danger')

    return render_template('login.html', form=form)


@bp.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Logged out.', 'success')
    return redirect(url_for('auth.login'))


@bp.route('/change-password', methods=['GET', 'POST'])
@login_required
def change_password():
    form = ChangePasswordForm()
    if form.validate_on_submit():
        if not current_user.check_password(form.current_password.data):
            flash('Невірний поточний пароль.', 'danger')
            return redirect(url_for('auth.change_password'))

        current_user.set_password(form.new_password.data)
        db.session.commit()
        flash('Пароль змінено успішно.', 'success')
        return redirect(url_for('users.profile'))

    return render_template('change_password.html', form=form)