
from flask import Blueprint, request, jsonify
from services.user_service import (
    create_user_service,
    get_user_service,
    get_all_users_service,
    update_user_service,
    delete_user_service
)

user_bp = Blueprint("users", __name__)

@user_bp.route("/users", methods=["POST"])
def create_user():
    return create_user_service(request.get_json())

@user_bp.route("/users/<int:user_id>", methods=["GET"])
def get_user(user_id):
    return get_user_service(user_id)

@user_bp.route("/users", methods=["GET"])
def get_all_users():
    return get_all_users_service()

@user_bp.route("/users/<int:user_id>", methods=["PUT"])
def update_user(user_id):
    return update_user_service(user_id, request.get_json())

@user_bp.route("/users/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    return delete_user_service(user_id)
