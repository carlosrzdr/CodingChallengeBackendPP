from re import compile
from app.models import Plate
from enchant.utils import levenshtein


def plate_is_valid(plate_number):
    """
    checks if a plate number satisfies the regular expression
    :param plate_number: str
    :return: regex match
    """
    plate_format = compile('^[A-Z]{1,3}-[A-Z]{1,2}[1-9]{1}[0-9]{0,3}$')
    return plate_format.match(plate_number)

def get_plates():
    """
    get all plates saved in the database
    :param plate_number: str
    :return: list
    """
    plates = Plate.query.all()
    result = []
    for plate in plates:
        result.append(row2dict(plate))
    return result

def search_plate_levenshtein(plate_number, levenshtein_distance):
    """
    search plates with a levenshtein distance equal or less to the specified plate number
    :param plate_number: str
    :param levenshtein_distance: int
    :return: list
    """
    plates = get_plates()
    result = []
    for entry in plates:
        if levenshtein(plate_number, entry['plate']) <= levenshtein_distance:
            result.append(entry)
    return result

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