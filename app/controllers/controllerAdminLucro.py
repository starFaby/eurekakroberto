from flask import request, render_template as render, flash
from app.database.database import *
from flask import g
from app.utils.fechahora import fechahora
from sqlalchemy.exc import SQLAlchemyError

class ControllerAdminLucro:

    def onGetControllerLucroList():
        try:
            result = 0
            return render("admin/adminLucro.html", result=result)
        except SQLAlchemyError as e:
            error = str(e.__dict__['orig'])
            print(error)
            return render('errors/error500.html')
    def onGetControllerLucroSave():
        try:
            sumaLucro = 0
            finLucro = 0
            pfsabalfechainicio = request.form['dFechaInicio']
            pfsabalfechafin = request.form['dFechaFin']
            lucro = Proforma.query.filter(Proforma.pfsabpfcreatedat.between(pfsabalfechainicio,pfsabalfechafin)).all()
            for item in lucro:
                sumaLucro += item.pfsabpftotal

            finLucro = sumaLucro * 0.05
            return render("admin/adminLucro.html", sumaLucro=sumaLucro, finLucro=finLucro)
        except SQLAlchemyError as e:
            error = str(e.__dict__['orig'])
            print(error)
            return render('errors/error500.html')