from database_setup import Base, User
from sqlalchemy.orm import sessionmaker
from flask import session as login_session

from views import session

def createUser(login_session):
    newUser = User(name=login_session['username'], email=login_session[
                   'email'], pic_url=login_session['picture'])
    session.add(newUser)
    session.commit()
    user = session.query(User).filter_by(email=login_session['email']).one()
    return user.id


def getUserInfo(user_id):
    user = session.query(User).filter_by(id=user_id).one()
    return user


def getUserID(email):
    try:
        user = session.query(User).filter_by(email=email).one()
        return user.id
    except:
        return None