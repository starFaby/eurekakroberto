from flask import request, render_template as render, g, redirect, url_for, flash
from app.database.database import *
from flask_login import current_user
from datetime import datetime
from sqlalchemy.exc import SQLAlchemyError

class ControllerClientCanasta:

    def onGetControllerClientCanastaList():
        try:
            
            userId = current_user.iduser
            userSelect = User.query.get(userId)
            fecha =  datetime.now()
            numberFact = g.fact
            sumaTotal = 0
            detalleFact = Detalleproforma.query.join(Producto, Detalleproforma.pfsabproductoid == Producto.pfsabprodid).add_columns(Detalleproforma.pfsabdpid , Detalleproforma.pfsabproductoid, Producto.pfsabprodnombre, Producto.pfsabproddetalle, Detalleproforma.pfsabdpcantidad, Detalleproforma.pfsabdprecio, Detalleproforma.pfsabdptotal).filter(Detalleproforma.pfsabdpestado == 1).filter(Detalleproforma.pfsabdpnumpf == numberFact)
            for item in detalleFact:
                sumaTotal += item.pfsabdptotal

            dateGeneral = {
                "userSelect": userSelect,
                "fecha": fecha,
                "numberFact": numberFact,
                "detalleFact": detalleFact,
                "sumaTotal": sumaTotal
            }
            print("dateGeneral")
            print(dateGeneral)

            return render('client/clientCanasta.html', dateGeneral=dateGeneral)
        except SQLAlchemyError as e:
            error = str(e.__dict__['orig'])
            print(error)
            return render('errors/error500.html')

    def onGetControllerClientProductUpdate(dpid, dpcant, pid):
        try:
            putDetalleProforma = Detalleproforma.query.get(dpid)
            putDetalleProforma.pfsabdpestado = 0

            putProducto = Producto.query.get(pid)
            pstock = int(putProducto.pfsabprodstock )
            ccanasta = int(dpcant)
            retornarProd = pstock + ccanasta
            putProducto.pfsabprodstock = retornarProd
            db.session.commit()
            
            return  redirect(url_for('rcnt.onGetControllerClientCanastaList'))
        except SQLAlchemyError as e:
            error = str(e.__dict__['orig'])
            print(error)
            return render('errors/error500.html')

    def onGetControllerClientSaveCanasta():
        try:
            pfsabpfnumpf = request.form["txtNumFact"]
            pfsabpftotal = request.form["txtSumaTotal"]
            updateProforma = Proforma.query.get(pfsabpfnumpf)
            updateProforma.pfsabpftotal = pfsabpftotal
            updateProforma.pfsabpfestado = 1
            db.session.commit()
            flash('Datos Actualizados', category='success')
            return redirect(url_for('clca.onGetControllerClientCategoriaList'))
        except SQLAlchemyError as e:
            error = str(e.__dict__['orig'])
            print(error)
            return render('errors/error500.html')
       

    