import os

MAIL_SERVER = os.environ.get('MAIL_SERVER')
MAIL_PORT = os.environ.get('MAIL_PORT')
MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
MAIL_USE_SSL = os.environ.get('MAIL_USE_SSL', True)
MAIL_USE_TLS= os.environ.get('MAIL_USE_TLS', False)
MAIL_SUPPRESS_SEND = os.environ.get('MAIL_SUPPRESS_SEND', False)
MAIL_DEFAULT_SENDER = os.environ.get('MAIL_DEFAULT_SENDER')