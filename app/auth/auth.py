import sys
from datetime import datetime
from flask import render_template as render, request, jsonify, redirect, url_for
from sqlalchemy.sql.elements import Null
from app.database.database import *

class Auth:

    def onGetAuth():
        return render('auth/auth.html')
    
    def onGetListAuth():
        allTasks = User.query.all()
        result = usersSchema.dump(allTasks)
        return jsonify(result)

    def onGetListOneAuth(self,id):
        pass
 
    def onGetCreateAuth():
        pfsabcedula = request.form['txtCedula']
        pfsabnombres = request.form['txtNombres']
        pfsabapellidos = request.form['txtApellidos']
        pfsabusername = request.form['txtUsername']
        pfsabemail = request.form['txtEmail']
        pfsabpassword = request.form['txtPassword']
        pfsabcellphone = request.form['txtCelphone']
        pfsabphone = request.form['txtCelphone']
        pfsabisadmin =  False
        pfsabavatar = 'https://res.cloudinary.com/dqmbrjl7jfs/image/upload/v1640009274/aux/noimage_b9edhb.jpg'
        pfsabestado = request.form['txtEstado']
        pfsabcreatedat = datetime.now().strftime('%x')
        
        newUser = User(pfsabcedula, pfsabnombres, pfsabapellidos, pfsabusername, pfsabemail, pfsabpassword, pfsabcellphone, pfsabphone, pfsabisadmin, pfsabavatar, pfsabestado, pfsabcreatedat)
        newUser.onGetSetPassword(pfsabpassword)
        db.session.add(newUser)
        db.session.commit()
        return redirect(url_for("loginin.onGetLogin"))

    def getUserByUsername(pfsabusername):
        return User.query.filter_by(pfsabusername = pfsabusername).first()

    def onGetUpdateAuth(self):
        pass

    def onGetDeleteAuth(self):
        pass


    