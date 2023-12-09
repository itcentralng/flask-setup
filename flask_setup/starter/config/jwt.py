from datetime import timedelta
import os


secret = os.environ.get('APP_SECRET')

# Jwt config
JWT_SECRET_KEY = secret
JWT_ACCESS_TOKEN_EXPIRES = timedelta(days=1)
JWT_REFRESH_TOKEN_EXPIRES = timedelta(days=60)
JWT_HEADER_TYPE = 'Bearer'
JWT_HEADER_NAME = 'Authorization'
