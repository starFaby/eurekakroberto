from flask import request, render_template as render, g, redirect, url_for, flash
from app.database.database import *
from sqlalchemy.exc import SQLAlchemyError
from flask_login import current_user
from datetime import datetime


class ControllerClientCarrito:

    def onGetControllerClientCarritoList(id):
        try:
            producto = Producto.query.get(id)
            if producto != []:
                return render('client/clientCarrito.html', producto=producto)
            else:
                return render('index.html')
        except SQLAlchemyError as e:
            error = str(e.__dict__['orig'])
            print(error)
            return render('errors/error500.html')
        
    def onGetControllerClientCarritoSaveProforma():
        try:
            pfsabpfnumpf = 0
            pfsabpfsubtotal = 0
            pfsabpfdto = 0
            pfsabpfiva = 0
            pfsabpftotal = 0
            pfsabpfestado = 0
            pfsabcatecreatedat = datetime.now()
            pfsabuserid = current_user.iduser
            #session.query(func.max(table_name.column_name)).all()
            numProf = Proforma.query.count()
            
            if numProf == None:
                pfsabpfnumpf = 1
            if numProf != None:
                pfsabpfnumpf = numProf + 1

            if pfsabpfnumpf != '' and pfsabpfsubtotal != '' and pfsabpfdto != '' and pfsabpfiva != '' and pfsabpftotal != '' and pfsabpfestado != '' and pfsabcatecreatedat!= '' and pfsabuserid != '':
                newProforma = Proforma(pfsabpfnumpf, pfsabpfsubtotal, pfsabpfdto, pfsabpfiva, pfsabpftotal, pfsabpfestado, pfsabcatecreatedat, pfsabuserid)
                db.session.add(newProforma)
                db.session.commit()
                flash('Guardado Correctamente', category='success')
                return redirect(url_for('clca.onGetControllerClientCategoriaList'))
            else:
                flash('LLene los campos completos porfabor', category='success')
                return redirect(url_for('clca.onGetControllerClientCategoriaList'))
        except SQLAlchemyError as e:
            error = str(e.__dict__['orig'])
            print(error)
            return render('errors/error500.html')
    
    
    def onGetControllerClientNumProforma():
        try:
            numberProf = 0
            if current_user.is_authenticated:
                userId = current_user.iduser
                numProf = Proforma.query.filter(Proforma.pfsabpftotal == 0 and Proforma.pfsabuserid == userId)
                for item in numProf:
                    numberProf = item.pfsabpfnumpf
                    return numberProf
        except SQLAlchemyError as e:
            error = str(e.__dict__['orig'])
            print(error)
            return render('errors/error500.html')

    def onGetControllerClientAnadirCanasta():
        try:
            userId = current_user.iduser
            pfsabpfnumpf = g.fact
            pfsabdpcantidad = request.form['txtCantidad']
            pfsabdprecio = request.form['txtPrecio']
            pfsabdptotal = request.form['txtPrecioFinal']
            pfsabdpestado = 1
            pfsabdpcreatedat = datetime.now()
            pfsabproductoid = request.form['txtProductoId']
            proformaid = Proforma.query.filter(Proforma.pfsabpftotal == 0 and Proforma.pfsabuserid == userId)
            pfsabproformaid = 0
            for item in proformaid:
                pfsabproformaid = item.pfsabpfid
            if pfsabpfnumpf != '' and pfsabdpcantidad != '' and pfsabdprecio != '' and pfsabdptotal != '' and pfsabdpestado != '' and pfsabdpcreatedat != '' and pfsabproductoid != '' and pfsabproformaid != '':
                newDetalleProforma = Detalleproforma(pfsabpfnumpf, pfsabdpcantidad, pfsabdprecio, pfsabdptotal, pfsabdpestado, pfsabdpcreatedat, pfsabproductoid, pfsabproformaid)
                db.session.add(newDetalleProforma)
                db.session.commit()
                ControllerClientCarrito.onGetUpdateProductoId(pfsabproductoid,pfsabdpcantidad)
                flash('Datos Actualizados', category='success')
                return redirect(url_for('rcnt.onGetControllerClientCanastaList'))
            else:
                flash('Campos vacios llene porfabor', category='success')
                return redirect(url_for('rcnt.onGetControllerClientCanastaList'))
        except SQLAlchemyError as e:
            error = str(e.__dict__['orig'])
            print(error)
            return render('errors/error500.html')

    @staticmethod   
    def onGetUpdateProductoId(pfsabproductoid, pfsabdpcantidad):
        try:
            stok = 0
            updateProduct = Producto.query.get(pfsabproductoid)
            stok = updateProduct.pfsabprodstock
            
            updateProdStok = int(stok) - int(pfsabdpcantidad)
            updateProduct.pfsabprodstock = updateProdStok
            if updateProduct.pfsabprodstock != 0:
                db.session.commit()
        except SQLAlchemyError as e:
            error = str(e.__dict__['orig'])
            print(error)
            return render('errors/error500.html')