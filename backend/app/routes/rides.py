from flask import Blueprint, jsonify, request
from app.models.database import parking_collection

bp = Blueprint('rides', __name__, url_prefix='/rides')

@bp.route('/', methods=['GET'])
def test_rides():
    return "Reached rides apis!"
