
'''
Marshmallow
--------------
'''

from projectname.model import *

from flask_marshmallow import Marshmallow

from projectname import app

ma = Marshmallow(app)

# Sample Marshmallow Schemas, copy the same style to make your own

class BookSchema(ma.Schema):
    class Meta:
        fields = ('id', 'title', 'author', 'price', 'isbn')
        model = Book

class AuthorSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'age', 'country')
        model = Author