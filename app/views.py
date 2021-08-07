from flask import Blueprint, render_template, request, jsonify, abort
import json
from app.plate import plateIsValid
from app.models import Plate

# Constants
SUCCESS_200 = json.dumps({'success':True}), 200, {'ContentType':'application/json'}

view = Blueprint("views", __name__)

def row2dict(row):
    """
    transforms SQLAlchemy response row into python dictionary
    :param row: Plate
    :return: dict
    """
    d = {}
    for column in row.__table__.columns:
        d[column.name] = str(getattr(row, column.name))

    return d

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
    :return: a json containing response codes if POST, a json containing plates data if GET
    """
    if request.method == 'POST':
        try:
            plate_number = request.form['plate']
        except:
            abort(400)

        plate_number = plate_number.upper()
        if plateIsValid(plate_number) is not None:
            plate = Plate(plate_number=plate_number)
            plate.save()
            return SUCCESS_200
        else:
            abort(422)

    if request.method == 'GET':
        plates = Plate.query.all()
        response = []
        for plate in plates:
            response.append(row2dict(plate))
        return jsonify(response)

@view.route("/search-plate", methods=["GET"])
def search_plate():
    """
    retrieves plates with levenshtein distance equal or less than the specified
    :return: a json containing plates found with levenshtein distance equal or less than the specified
    """

    return jsonify({'key':request.args['key'], 'levenshtein':request.args['levenshtein']})