import os
from sqlalchemy.pool import QueuePool

# Database configuration
SQLALCHEMY_DATABASE_URI= os.environ.get('DATABASE_URI')
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_ENGINE_OPTIONS = {
    "pool_pre_ping": True,
    'poolclass': QueuePool,
    'pool_size': 10,  # Number of connections to keep open inside the pool
    'max_overflow': 20,  # Number of extra connections to allow if pool is full
    'pool_timeout': 30,  # Maximum seconds to wait for a connection to become available
    }
