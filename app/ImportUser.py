from app.model import User
from app import db
from werkzeug.security import generate_password_hash

def import_user():
    for i in range(10):
        password_byte = str(i).encode('utf')
        user = User(username=str(i), password_hash=generate_password_hash(password_byte))
        db.session.add(user)
        db.session.commit()


if __name__ == '__main__':
    import_user()