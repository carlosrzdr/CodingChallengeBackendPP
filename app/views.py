from flask import Blueprint, render_template, request, jsonify
import json
from app.plate import plateIsValid
from app.models import Plate

# Constants
SUCCESS_200 = json.dumps({'success':True}), 200, {'ContentType':'application/json'}
ERROR_400 = json.dumps({'success':False}), 400, {'ContentType':'application/json'}
ERROR_422 = json.dumps({'success':False}), 422, {'ContentType':'application/json'}

view = Blueprint("views", __name__)

def row2dict(row):
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
            return ERROR_400

        plate_number = plate_number.upper()
        if plateIsValid(plate_number) is not None:
            plate = Plate(plate_number=plate_number)
            plate.save()
            return SUCCESS_200
        else:
            return ERROR_422

    if request.method == 'GET':
        plates = Plate.query.all()
        response = []
        for plate in plates:
            response.append(row2dict(plate))
        return jsonify(response)