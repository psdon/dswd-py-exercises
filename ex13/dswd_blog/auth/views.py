from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import current_user, login_user, logout_user
from .forms import SignInForm, SignUpForm
from ..models import User
from ..extensions import db

# Try :: url_prefix="/account"
bp = Blueprint("auth", __name__)


@bp.route("/sign-in/", methods=["GET", "POST"])
def sign_in():
    if current_user.is_authenticated:
        return redirect(url_for("blog.home"))

    form = SignInForm()

    if form.validate_on_submit():
        user = form.username_or_email.data
        password = form.password.data
        user_obj = User.query.filter(
            (User.email == user) | (User.username == user)
        ).first()

        if user_obj and user_obj.check_password(password):
            login_user(user_obj)

        else:
            flash("Incorrect username or password", "warning")
            return render_template("auth/sign_in/index.html", form=form)

        # Be Careful, URL Redirect Vulnerability
        safe_redirect = None
        if request.args.get("next"):
            safe_redirect = f"{request.host_url}{request.args.get('next').strip('/')}"

        return redirect(safe_redirect or url_for("public.blog"))
    return render_template("auth/sign_in/index.html", form=form)


@bp.route("/sign-out/")
def sign_out():
    """Logout."""
    logout_user()
    flash("You have signed out successfully", category="success")
    return redirect(url_for("public.home"))


@bp.route("/sign-up/", methods=["GET", "POST"])
def sign_up():
    if current_user.is_authenticated:
        return redirect(url_for("public.blog"))

    form = SignUpForm()

    if form.validate_on_submit():
        new_user = User(
            username=form.username.data,
            email=form.email.data,
            password=form.password.data,
        )

        db.session.add(new_user)
        try:
            db.session.commit()
            flash("You have signed up successfully. You can now sign-in", "success")
            return redirect(url_for("auth.sign_in"))
        except Exception:
            db.session.rollback()
            flash("Oops, an error occurred. Please try again later.", "warning")

    return render_template("auth/sign_up/index.html", form=form)