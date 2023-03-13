from flask import request, render_template as render
from app.database.database import *

class ControllerClientCarrito:

    def onGetControllerClientCarritoList(id):
        producto = Producto.query.get(id)
        if producto != []:
            return render('client/clientCarrito.html', producto=producto)
        else:
            return render('index.html')