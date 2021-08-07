from flask import Blueprint, render_template, request, jsonify, abort
import json
from app.plate import get_plates, plate_is_valid, search_plate_levenshtein
from app.models import Plate

# Constants
SUCCESS_200 = json.dumps({'success':True}), 200, {'ContentType':'application/json'}

view = Blueprint("views", __name__)

@view.route("/")
def index():
    """
    shows main page
    """
    return render_template("index.html")

@view.route("/plates")
def plates():
    """
    shows plates page containing the funcionalities for saving and retrieving plates
    """
    return render_template("plates.html")

@view.route("/search")
def search():
    """
    shows search page containing the funcionality for searching plates
    """
    return render_template("search.html")

@view.route("/plate", methods=["POST", "GET"])
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

@view.route("/search-plate", methods=["GET"])
def search_plate():
    """
    retrieves plates with levenshtein distance equal or less than the specified
    :return: a json containing plates found with levenshtein distance equal or less than the specified
    """
    try:
        key = request.args['key'].upper()
        levenshtein = int(request.args['levenshtein'])
    except:
        abort(400)

    if plate_is_valid(key) is not None:
        response = search_plate_levenshtein(key, levenshtein)
        return jsonify(response)
    else:
        abort(422)