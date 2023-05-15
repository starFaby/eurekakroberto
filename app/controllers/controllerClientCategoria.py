from flask import request, render_template as render
from sqlalchemy.exc import SQLAlchemyError
from app.database.database import *
from flask import g

class ControllerClientCategoria:

    def onGetControllerClientCategoriaList():
        try:
            categorias = Categoria.query.filter(Categoria.pfsabcateestado == 1)
            return render('client/clientCategoria.html', categorias=categorias)
        except SQLAlchemyError as e:
            error = str(e.__dict__['orig'])
            print(error)
            return render('errors/error500.html')
            #print("Something went wrong: mysql failed")
