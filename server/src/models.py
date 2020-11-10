""" Contains objects holding state. These objects should be simple. """
import flask_login


class Serializable:
    def serialize(self):
        return {c: getattr(self, c) for c in vars(self).keys()}


class User(flask_login.UserMixin, Serializable):
    def __init__(self, id, email, password, created_at):
        self.id = id
        self.email = email
        self.password = password
        self.created_at = created_at

    def serialize(self):
        d = super().serialize()
        del d["password"]
        return d
