import datetime
import os


secret = os.getenv('APP_SECRET')

# Jwt config
JWT_SECRET_KEY = secret
JWT_BLACKLIST_ENABLED = True
JWT_BLACKLIST_TOKEN_CHECKS = ['access', 'refresh']
JWT_ACCESS_TOKEN_EXPIRES = datetime.datetime.utcnow() + datetime.timedelta(days=1)
JWT_REFRESH_TOKEN_EXPIRES = datetime.datetime.utcnow() + datetime.timedelta(days=1)
JWT_HEADER_TYPE = 'Bearer'
JWT_HEADER_NAME = 'Authorization'
