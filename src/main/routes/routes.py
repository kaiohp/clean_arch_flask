from flask import Blueprint, jsonify, request

from src.main.adapters.request_adapter import request_adapter
from src.main.composers.user_finder_compose import user_finder_compose
from src.main.composers.user_register_compose import user_register_compose

user_routes_bp = Blueprint('user_routes', __name__)


@user_routes_bp.route('/user/find', methods=['GET'])
def find_user():
    http_response = request_adapter(request, user_finder_compose())

    return jsonify(http_response.status_code, http_response.body)


@user_routes_bp.route('/user', methods=['POST'])
def register_user():
    http_response = request_adapter(request, user_register_compose())

    return jsonify(http_response.status_code, http_response.body)
