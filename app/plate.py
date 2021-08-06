from re import compile

def plateIsValid(plate_number):
    plate_format = compile('^[A-Z]{1,3}-[A-Z]{1,2}[1-9]{1}[0-9]{0,3}$')
    return plate_format.match(plate_number)