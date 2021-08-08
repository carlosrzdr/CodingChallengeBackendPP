from flask import Blueprint, render_template, request, jsonify, abort
from app.actions.plate_actions import plate_is_valid, search_plate_levenshtein

bp = Blueprint("search_plate", __name__)

@bp.route("/search")
def search():
    """
    shows search page containing the funcionality for searching plates
    """
    return render_template("search.html")

@bp.route("/search-plate", methods=["GET"])
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

    if key=='':
        abort(400)

    response = search_plate_levenshtein(key, levenshtein)
    return jsonify(response)