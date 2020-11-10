""" Entry point for the server."""

import flask
import flask_login

from src import const, util


def register_error_handlers(app):
    @app.errorhandler(util.HTTPError)
    def handle_invalid_usage(error):
        response = flask.jsonify(error.to_dict())
        response.status_code = error.status_code
        return response


def create_app():
    app = flask.Flask(__name__)
    app.secret_key = b"skfjf8239#(94kfjkdgs8#*4jjfdksjg9#0gkj"  # TODO store secret key in config file
    app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 1  # disable caching
    app.config["DATABASE"] = const.DB_PATH

    with app.app_context():
        from src import api, db, auth

        db.init_app(app)
        app.register_blueprint(api.api)
        login_manager = flask_login.LoginManager()
        login_manager.init_app(app)
        auth.register_login_manager_request_loader(login_manager)
        register_error_handlers(app)

    return app


if __name__ == "__main__":
    application = create_app()
    application.run(debug=True)
