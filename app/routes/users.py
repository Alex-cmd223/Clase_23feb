from flask import Blueprint, request, jsonify


users_bp = Blueprint('users', __name__)

# Endpoint 4: Consultar progreso 
@users_bp.route('/progreso', methods=['POST'])
def consultar_progreso():
    data = request.json
    return jsonify({
        "status": "success", 
        "facil_completados": 8,
        "medio_completados": 3, 
        "dificil_completados": 0
    }), 200

# Endpoint 5: Actualizar perfil 
@users_bp.route('/perfil', methods=['PUT'])
def actualizar_perfil():
    data = request.json
    return jsonify({
        "status": "success",
        "mensaje": "Perfil actualizado"
    }), 200