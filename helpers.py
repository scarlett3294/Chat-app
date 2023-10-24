from model import User, db

def is_name_registered(username):
    return User.query.filter_by(username=username).first() is not None

def register_name(username):
    new_user = User()
    new_user.username = username
    db.session.add(new_user)
    db.session.commit()


