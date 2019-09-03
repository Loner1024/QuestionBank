from app import db, login
from flask_login import UserMixin


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    password_hash = db.Column(db.String(128))


@login.user_loader
def load_user(id):
    # id 以字符串传入，需要转换为 int
    return User.query.get(int(id))
