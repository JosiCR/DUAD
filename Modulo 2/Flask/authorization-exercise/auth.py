
from functools import wraps

from flask import jsonify, request

from jwt_manager import jwt_manager
from user_repository import user_repository


def require_auth(required_role=None):
    def decorator(view_function):
        @wraps(view_function)
        def wrapped(*args, **kwargs):
            authorization = request.headers.get("Authorization", "")

            if not authorization.startswith("Bearer "):
                return jsonify(error="Authentication required"), 401

            token = authorization.removeprefix("Bearer ").strip()
            decoded = jwt_manager.decode_token(token, "access")

            if decoded is None:
                return jsonify(error="Invalid or expired access token"), 401

            user = user_repository.get_by_id(decoded["id"])

            if user is None:
                return jsonify(error="User not found"), 401

            if required_role is not None and user["role"] != required_role:
                return jsonify(error="Insufficient permissions"), 403

            return view_function(*args, **kwargs)

        return wrapped
    return decorator
