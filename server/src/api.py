""" Contains all api endpoints. """
import flask
import flask_login
import werkzeug.security

from src import auth, repositories, util

api = flask.Blueprint('api', __name__)


@api.route("/")
def index():
    return flask.jsonify("Hello world")


@api.route("/register", methods=["POST"])
def register():
    body = flask.request.get_json()

    if body is None:
        raise util.HTTPError("Invalid parameters", status_code=401)

    email = body.get("email")
    password = body.get("password")

    if not email or not password:
        raise util.HTTPError(
            "Email and password can not be empty", status_code=401)

    if repositories.users.get_by_email(email):
        raise util.HTTPError("User with this email address already exists", status_code=401)

    password_hash = werkzeug.security.generate_password_hash(password)
    repositories.users.create(email, password_hash)
    return flask.jsonify("success")


@api.route("/authenticate", methods=["POST"])
def login():
    email = flask.request.json.get("email")
    password = flask.request.json.get("password")

    if not email or not password:
        raise util.HTTPError(
            "Email and password can not be empty", status_code=401)

    user = repositories.users.get_by_email(email)

    if not user:
        raise util.HTTPError("Incorrect login details", status_code=401)

    if not werkzeug.security.check_password_hash(user.password, password):
        raise util.HTTPError("Incorrect login details", status_code=401)

    auth_token = auth.encode_auth_token(user.id)

    response = {
        'user_id': user.id,
        'email': email,
        'auth_token': auth_token.decode()
    }

    flask_login.login_user(user)

    return flask.jsonify(response)


@api.route("/logout")
def logout():
    flask_login.logout_user()


@api.route("/private")
@flask_login.login_required
def private():
    return flask.jsonify("Welcome to the private area")


@api.route("/users")
@flask_login.login_required
def get_users():
    serialized = list(map(lambda u: u.serialize(), repositories.users.get_all()))
    return flask.jsonify(users=serialized)


@api.route("/users/<user_id>")
@flask_login.login_required
def get_user_by_id(user_id):
    user = repositories.users.get_by_id(user_id)

    if user is None:
        raise util.HTTPError("User not found", status_code=401)

    return flask.jsonify(users=user.serialize())
