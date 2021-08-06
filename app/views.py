from flask import Blueprint, render_template

view = Blueprint("views", __name__)

@view.route("/", methods=["GET"])
def index():
    """
    shows main page
    """
    return render_template("index.html")

@view.route("/plate", methods=["POST", "GET"])
def plate():
    """
    inserts a new plate into database and retrieves all plates
    """
    return render_template("plate.html")