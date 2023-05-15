from flask import request, render_template as render
from app.database.database import *
from sqlalchemy.exc import SQLAlchemyError

class ControllerClientPromociones:

    def onGetControllerClientPromocionesList():
        try:
            promociones = Promociones.query.join(Producto, Promociones.pfsabproductoid == Producto.pfsabprodid).add_columns(Producto.pfsabprodnombre, Producto.pfsabprodimage, Producto.pfsabproddetalle , Promociones.pfsabpromfechainicio, Promociones.pfsabpromfechafin).filter(Promociones.pfsabpromestado == 1)
            return render('client/clientPromociones.html', promociones=promociones)
        except SQLAlchemyError as e:
            error = str(e.__dict__['orig'])
            print(error)
            return render('errors/error500.html')
    