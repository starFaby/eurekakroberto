from flask import request, render_template as render , redirect, url_for
from flask_login import current_user
from app.database.database import *

class ControllerClientProducto:

    def onGetControllerProductoList(id):
        productos = Producto.query.filter(Producto.pfsabcategoriaid == id)
        return render("client/clientProducto.html", productos = productos)

