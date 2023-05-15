import sys
from datetime import datetime
from flask import render_template as render, request, jsonify, redirect, url_for
from sqlalchemy.sql.elements import Null
from sqlalchemy.exc import SQLAlchemyError
from app.database.database import *

class Auth:

    def onGetAuth():
        return render('auth/auth.html')
    
    def onGetListAuth():
        try:
            allTasks = User.query.all()
            result = usersSchema.dump(allTasks)
            return jsonify(result)
        except SQLAlchemyError as e:
            error = str(e.__dict__['orig'])
            print(error)
            return render('errors/error500.html')

    def onGetListOneAuth(self,id):
        pass
 
    def onGetCreateAuth():
        try:
            pfsabcedula = request.form['txtCedula']
            pfsabnombres = request.form['txtNombres']
            pfsabapellidos = request.form['txtApellidos']
            pfsabusername = request.form['txtUsername']
            pfsabemail = request.form['txtEmail']
            pfsabpassword = request.form['txtPassword']
            pfsabdireccion = request.form['txtDireccion']
            pfsabcellphone = request.form['txtCellphone']
            pfsabphone = request.form['txtPhone']
            pfsabisadmin =  False
            pfsabavatar = 'https://res.cloudinary.com/dqmbrjl7jfs/image/upload/v1640009274/aux/noimage_b9edhb.jpg'
            pfsabestado = request.form['txtEstado']
            pfsabcreatedat = datetime.now()
            
            newUser = User(pfsabcedula, pfsabnombres, pfsabapellidos, pfsabusername, pfsabemail, pfsabpassword, pfsabdireccion, pfsabcellphone, pfsabphone, pfsabisadmin, pfsabavatar, pfsabestado, pfsabcreatedat)
            newUser.onGetSetPassword(pfsabpassword)
            db.session.add(newUser)
            db.session.commit()
            return redirect(url_for("loginin.onGetLogin"))
        except SQLAlchemyError as e:
            error = str(e.__dict__['orig'])
            print(error)
            return render('errors/error500.html')

    def getUserByUsername(pfsabusername):
        try:
            return User.query.filter_by(pfsabusername = pfsabusername).first()
        except SQLAlchemyError as e:
            error = str(e.__dict__['orig'])
            print(error)
            return render('errors/error500.html')
    def onGetUpdateAuth(self):
        pass

    def onGetDeleteAuth(self):
        pass


    