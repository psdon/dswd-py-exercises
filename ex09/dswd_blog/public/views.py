from flask import Blueprint, render_template
from dswd_blog.models import Blog
from flask_login import login_required

bp = Blueprint("public", __name__)


@bp.route("/")
def home():
    return render_template("public/home/index.html")


@bp.route("/blog")
@login_required
def blog():
    blogs = Blog.query.all()

    return render_template("public/blog/index.html", blogs=blogs)
