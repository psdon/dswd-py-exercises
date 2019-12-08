from flask import Blueprint, render_template

bp = Blueprint("public", __name__)


@bp.route("/")
def home():
    return render_template("public/home/index.html")


@bp.route("/blog")
def blog():
    return render_template("public/blog/index.html")
