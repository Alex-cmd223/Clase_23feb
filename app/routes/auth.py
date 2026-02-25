from flask import Blueprint, request, jsonify


auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/usuarios/login', methods=['POST'])
def login():
    # Endpoint 1 
    return jsonify({"autenticado": True, "user_id": 223, "username": "Alex"}), 200