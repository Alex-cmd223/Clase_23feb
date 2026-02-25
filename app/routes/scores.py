from flask import Blueprint, request, jsonify

scores_bp = Blueprint('scores', __name__)

# Endpoint 2: Registrar 
@scores_bp.route('/usuarios/puntaje/registrar', methods=['PUT'])
def registrar_puntaje():
    data = request.json
    return jsonify({"status": "success", "Mensaje": "Puntaje guardado"}), 200

# Endpoint 3: Leaderboard
@scores_bp.route('/usuarios/puntaje/leaderboard', methods=['GET'])
def get_leaderboard():
    return jsonify([
        {"rank": 1, "user": "Alex", "score": 1500},
        {"rank": 2, "user": "Edu", "score": 1200}
    ]), 200