from datetime import datetime
from flask import request, render_template as render, flash, redirect, url_for
from app.database.database import *


class ControllerAdminCategoria:

    def controllerAdminCategoriaList(page):
        page = page
        pages = 5
        categorias = Categoria.query.order_by(Categoria.pfsabcateid.asc()).paginate(page, pages,error_out=False)
        if categorias != []:
            if request.method == 'POST' and 'tag' in request.form:
                tag = request.form["tag"]
                search = "%{}%".format(tag)
                categorias = Categoria.query.filter(Categoria.pfsabcatenombre.like(search)).paginate(per_page=pages,error_out=False)
                return render("admin/adminCategoria.html", categorias=categorias, tag = tag)
            else:
                flash('Categorias Listadas', category='success')
                return render("admin/adminCategoria.html", categorias=categorias)
        else:
            flash('No existe categorias', category='success')
            return render("admin/adminCategoria.html", categorias=categorias)
        

    def onGetControllerAdminCategoriaSave():
        pfsabcatenombre = request.form['txtNombre']
        pfsabcateimage = request.form['txtImage']
        pfsabcatedetalle = request.form['txtDetalle']
        pfsabcateestado = request.form['selectEstado']
        pfsabcatecreatedat = datetime.now().strftime('%d/%m/%Y')
        if pfsabcatenombre != '' and pfsabcateimage != '' and pfsabcatedetalle != '' and pfsabcateestado != 'Elija...':
            newcategoria = Categoria(pfsabcatenombre, pfsabcateimage, pfsabcatedetalle, pfsabcateestado, pfsabcatecreatedat)
            db.session.add(newcategoria)
            db.session.commit()
            flash('Guardado Correctamente', category='success')
            return redirect(url_for('adcate.controllerAdminCategoriaList'))
        else:
            flash('LLene los campos completos porfabor', category='success')
            return redirect(url_for('adcate.controllerAdminCategoriaList'))

    def onGetControllerAdminCategoriaUpdate(id):
        categoria = Categoria.query.get(id)
        if request.method == 'POST':
            categoria.pfsabcatenombre = request.form['txtNombre']
            categoria.pfsabcateimage = request.form['txtImage']
            categoria.pfsabcatedetalle = request.form['txtDetalle']
            categoria.pfsabcateestado = request.form['selectEstado']
            if categoria.pfsabcatenombre != '' and categoria.pfsabcateimage != '' and categoria.pfsabcatedetalle != '' and categoria.pfsabcateestado != 'Elija...':
                db.session.commit()
                flash('Datos Actualizados', category='success')
                return redirect(url_for('adcate.controllerAdminCategoriaList'))
            else:
                flash('Campos vacios llene porfabor', category='success')
                return redirect(url_for('adcate.controllerAdminCategoriaList'))

        return render("modal/modalAdminCateUpdate.html", categoria = categoria)

    def onGetControllerAdminCategoriaDelete(id):
        categoria = Categoria.query.get(id)
        if categoria.id >= 0:
            db.session.delete(categoria)
            db.session.commit()
            flash('Categoria eliminada', category='danger')
            return redirect(url_for('adcate.controllerAdminCategoriaList'))
        else:
            flash('Error en el servidor', category='danger')
            return redirect(url_for('adcate.controllerAdminCategoriaList'))

    
