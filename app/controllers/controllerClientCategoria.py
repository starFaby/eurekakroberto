from flask import request, render_template as render
from app.database.database import *

class ControllerClientCategoria:

    def onGetControllerClientCategoriaList():
        categorias = Categoria.query.filter(Categoria.pfsabcateestado == 1)
        return render('client/clientCategoria.html', categorias=categorias)
      