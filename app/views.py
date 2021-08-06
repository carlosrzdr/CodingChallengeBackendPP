from flask import Blueprint, render_template, request, jsonify
import json

view = Blueprint("views", __name__)

@view.route("/")
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
    if request.method == 'POST':
        plate_number = request.form['plate']
        return json.dumps({'success':False}), 400, {'ContentType':'application/json'}

    return render_template("plate.html")