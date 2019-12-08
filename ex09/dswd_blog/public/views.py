from flask import Blueprint, render_template
from dswd_blog.models import Blog

bp = Blueprint("public", __name__)


@bp.route("/")
def home():
    return render_template("public/home/index.html")


@bp.route("/blog")
def blog():
    blogs = Blog.query.all()

    return render_template("public/blog/index.html", blogs=blogs)
