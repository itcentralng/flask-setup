from flask import Blueprint

from app.__blueprint__.model import *
from app.__blueprint__.schema import *
bp = Blueprint('__blueprint__', __name__)

@bp.get('/index')
def index():
    return '__blueprint__ Works'