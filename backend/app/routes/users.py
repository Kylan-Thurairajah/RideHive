from flask import Blueprint, jsonify, request, Response
from app.models.database import users_collection
from app.models.user_model import UserModel

bp = Blueprint('users', __name__, url_prefix='/users')

@bp.route('/', methods=['GET'])
def get_users():
    users = list(users_collection.find({}, {'_id': 0}))
    return jsonify(users)

@bp.route('/add', methods=['POST'])
def add_user():
    """
    Add a new user to the database.
    """
    try:
        # Parse and validate the incoming data using UserModel
        data = request.json
        user = UserModel(**data)
        
        print(user)

        # Insert the validated user data into the database
        result = users_collection.insert_one(user.model_dump(by_alias=True))

        return jsonify({"inserted_id": str(result.inserted_id)}), 201

    except Exception as e:
        return jsonify({"error": str(e)}), 400

