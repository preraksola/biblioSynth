from cgi import FieldStorage


def get_args():
    form = FieldStorage() #stores form data (field name, value)
    di = {}
    for key in form:
        di[key] = form[key].value #get the value for a field
        print di[key]
    return di
