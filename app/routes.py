# In routes.py

from flask import Blueprint, request, jsonify
from app.models import User
from app.database import db

api_blueprint = Blueprint('api', __name__)

# API Endpoints to create users and retrieve users
# POST /api/users
@api_blueprint.route('/api/users', methods=['POST'])
def create_user():
    try:
        data = request.get_json()

        # Validate and process input data
        if 'username' not in data or 'email' not in data or 'password' not in data:
            return jsonify({'error': 'Missing required fields'}), 400

        # Check if the username or email is already taken
        if User.query.filter_by(username=data['username']).first() or User.query.filter_by(email=data['email']).first():
            return jsonify({'error': 'Username or email already taken'}), 400

        # Create a new user
        new_user = User(username=data['username'], email=data['email'], password=data['password'])

        # If using a database, add and commit the new user
        db.session.add(new_user)
        db.session.commit()

        return jsonify({'message': 'User created successfully'}), 201

    except Exception as e:
        return jsonify({'error': str(e)}), 500

# GET /api/users/{user_id}
@api_blueprint.route('/api/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    try:
        # If using a database, retrieve the user by user ID
        user = User.query.get(user_id)

        if user:
            return jsonify({
                'user_id': user.id,
                'username': user.username,
                'email': user.email
            }), 200
        else:
            return jsonify({'error': 'User not found'}), 404

    except Exception as e:
        return jsonify({'error': str(e)}), 500
