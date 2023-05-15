from flask import request, render_template as render , redirect, url_for
from flask_login import current_user
from app.database.database import *
from sqlalchemy.exc import SQLAlchemyError

class ControllerClientProducto:

    def onGetControllerProductoList(id):
        try:
            productos = Producto.query.filter(Producto.pfsabcategoriaid == id).filter(Producto.pfsabprodstock >= 1)
            return render("client/clientProducto.html", productos = productos)
        except SQLAlchemyError as e:
            error = str(e.__dict__['orig'])
            print(error)
            return render('errors/error500.html')
