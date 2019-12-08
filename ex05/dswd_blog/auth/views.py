from flask import Blueprint

# Try :: url_prefix="/account"
bp = Blueprint("auth", __name__)


@bp.route("/sign-in")
def sign_in():
    return "Sign In Page"
