from flask import Blueprint, jsonify, request

from src.erros.error_handler import handle_error
from src.main.adapters.request_adapter import request_adapter
from src.main.composers.user_finder_compose import user_finder_compose
from src.main.composers.user_register_compose import user_register_compose
from src.validator.user_finder_validator import user_finder_validator
from src.validator.user_register_validator import user_register_validator

user_routes_bp = Blueprint('user_routes', __name__)


@user_routes_bp.route('/user/find', methods=['GET'])
def find_user():
    try:
        user_finder_validator(request)
        http_response = request_adapter(request, user_finder_compose())
    except Exception as error:
        http_response = handle_error(error)

    return jsonify(http_response.status_code, http_response.body)


@user_routes_bp.route('/user', methods=['POST'])
def register_user():
    try:
        user_register_validator(request)
        http_response = request_adapter(request, user_register_compose())
    except Exception as error:
        http_response = handle_error(error)

    return jsonify(http_response.status_code, http_response.body)
