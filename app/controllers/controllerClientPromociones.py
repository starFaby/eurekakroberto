from flask import request, render_template as render
from app.database.database import *
import json

class ControllerClientPromociones:

    def onGetControllerClientPromocionesList():
        promociones = Promociones.query.join(Producto, Promociones.pfsabproductoid == Producto.pfsabprodid).add_columns(Producto.pfsabprodnombre, Producto.pfsabprodimage, Producto.pfsabproddetalle , Promociones.pfsabpromfechainicio, Promociones.pfsabpromfechafin).filter(Promociones.pfsabpromestado == 1)
        return render('client/clientPromociones.html', promociones=promociones)