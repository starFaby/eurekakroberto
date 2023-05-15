from app.database.database import *
from flask import render_template as render
from sqlalchemy.exc import SQLAlchemyError

def getUserByUsername(username):
    try:
        return User.query.filter_by(username = username)
    
    except SQLAlchemyError as e:
            error = str(e.__dict__['orig'])
            print(error)
            return render('errors/error500.html')