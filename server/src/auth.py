""" Contains logic related to authentication and authorization. """
import datetime
import logging

import jwt
from flask import current_app
from src import repositories

logger = logging.getLogger(__name__)


def encode_auth_token(user_id):
    """
    Generates the Auth Token
    :return: string
    """
    payload = {
        'exp': datetime.datetime.utcnow() + datetime.timedelta(days=0, seconds=3600),
        'iat': datetime.datetime.utcnow(),
        'sub': user_id
    }
    return jwt.encode(
        payload,
        current_app.config.get('SECRET_KEY'),
        algorithm='HS256'
    )


def decode_auth_token(auth_token):
    """
    Decodes the auth token
    :param auth_token:
    :return: integer|string
    """
    try:
        payload = jwt.decode(auth_token, current_app.config.get('SECRET_KEY'))
        return payload['sub']
    except jwt.ExpiredSignatureError:
        logger.warning("Token is expired")
        return None
    except jwt.InvalidTokenError:
        logger.warning("Token is invalid")
        return None


def register_login_manager_request_loader(login_manager):
    @login_manager.request_loader
    def load_user_from_request(request):
        api_key = request.headers.get('Authorization')

        if api_key:
            try:
                api_key = api_key.split("Bearer ")[1]
            except IndexError:
                api_key = None

        if not api_key:
            api_key = request.args.get('api_key')

        if not api_key:
            return None

        user_id = decode_auth_token(api_key)

        if user_id:
            return repositories.users.get_by_id(user_id)

        return None
