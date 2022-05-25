
'''
Marshmallow
--------------
'''

from projectname.model import *

from flask_marshmallow import Marshmallow

from projectname import app

ma = Marshmallow(app)

