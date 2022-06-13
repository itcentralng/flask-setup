from flask import Blueprint

from .model import *
from .schema import *
bp = Blueprint('__blueprint__', __name__)

@bp.post('/index')
def index():
    return '__blueprint__ Works'