
'''
blueprintname
--------------
'''
from flask import Blueprint


blueprintname = Blueprint('blueprintname', __name__, url_prefix='/blueprintname')

@blueprintname.route('/test-route')
def test_route():
    return {'status': 'OK'}
        