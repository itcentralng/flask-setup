
'''
MODEL
--------------
'''
from flask_sqlalchemy import SQLAlchemy
# TODO: if you want to use flask-login in your project, you need to install it first
# from flask_login import UserMixin
# from werkzeug.security import generate_password_hash as gph, check_password_hash as cph

db = SQLAlchemy()

#TODO: This is a model Sample with flask login usermixn, modify it to your needs
# class User(db.Model, UserMixin):
#     id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String)
#     name = db.Column(db.String)
#     gender = db.Column(db.String)
#     phone = db.Column(db.String)
#     email = db.Column(db.String)
#     password = db.Column(db.String)
#     def set_password(self, password):
#         self.password = gph(password)
#         return True
#     def is_verified(self, password):
#         return cph(self.password, password)
        