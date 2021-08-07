from flask import Blueprint, render_template, request, abort, jsonify
import json
from app.models import Plate
from app.actions.plate_actions import get_plates, plate_is_valid

# Constants
SUCCESS_200 = json.dumps({'success':True}), 200, {'ContentType':'application/json'}

bp = Blueprint("plate", __name__)

@bp.route("/")
@bp.route("/plates")
def plates():
    """
    shows plates page containing the funcionalities for saving and retrieving plates
    """
    return render_template("plates.html")

@bp.route("/plate", methods=["POST", "GET"])
def plate():
    """
    inserts a new plate into database and retrieves all plates
    :return: HTTP response codes if POST, a json containing plates data if GET
    """
    if request.method == 'POST':
        plate_number = request.form['plate'].upper()
        
        if not plate_number:
            abort(400)

        if plate_is_valid(plate_number) is not None:
            plate = Plate(plate_number=plate_number)
            plate.save()
            return SUCCESS_200
        else:
            abort(422)

    if request.method == 'GET':
        response = get_plates()
        return jsonify(response)