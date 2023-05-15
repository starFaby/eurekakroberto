from flask import request, render_template as render, flash
from app.database.database import *
from flask import g
from datetime import datetime
from sqlalchemy.exc import SQLAlchemyError

class ControllerAdminCanastaPdf:

    def onGetControllerAdminCanastaPdf(user , cnst):
        try:
            numCanasta = 0
            valorCanastaTotal = 0
            fecha =  datetime.now()
            userSelect = User.query.get(user)
            detalleFact = Proforma.query.join(Detalleproforma, Proforma.pfsabpfnumpf == Detalleproforma.pfsabproformaid).join(Producto,Detalleproforma.pfsabproductoid == Producto.pfsabprodid ).add_columns(Producto.pfsabprodnombre, Producto.pfsabproddetalle, Detalleproforma.pfsabdpcantidad, Detalleproforma.pfsabdprecio, Detalleproforma.pfsabdptotal, Proforma.pfsabpfnumpf ,Proforma.pfsabpftotal).filter(Detalleproforma.pfsabdpnumpf == cnst)
            for item in detalleFact:
                valorCanastaTotal = item.pfsabpftotal

            for item in detalleFact:
                numCanasta = item.pfsabpfnumpf
            return render("admin/adminCanastaPdf.html", userSelect=userSelect, detalleFact=detalleFact, valorCanastaTotal=valorCanastaTotal, numCanasta=numCanasta, fecha=fecha)
       
        except SQLAlchemyError as e:
            error = str(e.__dict__['orig'])
            print(error)
            return render('errors/error500.html')