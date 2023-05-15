from flask import request, render_template as render, flash
from app.database.database import *
from flask import g
from sqlalchemy.exc import SQLAlchemyError

class ControllerClients:

    def onGetControllerClientsList(page):
        try:
            page = page
            pages = 5
            clients = User.query.order_by(User.pfsabid.asc()).paginate(page=page, per_page=pages ,error_out=False)
            if clients != []:
                if request.method == 'POST' and 'tag' in request.form:
                    tag = request.form["tag"]
                    search = "%{}%".format(tag)
                    clients = User.query.filter(User.pfsabcedula.like(search)).paginate(per_page=pages,error_out=False)
                    return render("admin/adminClientes.html", clients=clients, tag = tag)
                else:
                    flash('Categorias Listadas', category='success')
                    return render("admin/adminClientes.html", clients=clients)
            else:
                flash('No existe categorias', category='success')
                return render("admin/adminClientes.html", clients=clients)
        except SQLAlchemyError as e:
            error = str(e.__dict__['orig'])
            print(error)
            return render('errors/error500.html')
