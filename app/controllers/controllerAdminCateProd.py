from datetime import datetime
from flask import request, render_template as render, flash, redirect, url_for
from app.database.database import *


class ControllerAdminCateProd:

    def controllerAdminCateProdList(page):
        page = page
        pages = 5
        cateProd = Producto.query.order_by(Producto.pfsabprodid.asc()).paginate(page, pages,error_out=False)
        categorias = Categoria.query.all()
        if cateProd != [] or categorias != []:
            if request.method == 'POST' and 'tag' in request.form:
                tag = request.form["tag"]
                search = "%{}%".format(tag)
                cateProd = Producto.query.filter(Producto.pfsabprodnombre.like(search)).paginate(per_page=pages,error_out=False)
                return render("admin/adminCateProd.html", cateProd=cateProd, categorias=categorias, tag = tag)
            else:    
                flash('Producto Listadas', category='success')
                return render("admin/adminCateProd.html", cateProd=cateProd, categorias=categorias)
        else:
            flash('No existe categorias', category='success')
            return render("admin/adminCateProd.html", cateProd=cateProd, categorias=categorias)

    def onGetControllerAdminCateProdSave():
        pfsabprodnombre = request.form['txtNombre']
        pfsabprodimage = request.form['txtImage']
        pfsabproddetalle = request.form['txtDetalle']
        pfsabprodprecio = request.form['txtPrecio']
        pfsabprodstock = request.form['txtStock']
        pfsabprodestado = request.form['selectEstado']
        pfsabprodcreatedat = datetime.now().strftime('%x')
        categoriaid = request.form['selectCategoria']
        if pfsabprodnombre != '' and pfsabprodimage != '' and pfsabproddetalle != ''and pfsabprodprecio != ''and pfsabprodstock != '' and pfsabprodestado != 'Elija...' and categoriaid != 'Elija...':
            newcateprod = Producto(pfsabprodnombre, pfsabprodimage, pfsabproddetalle,pfsabprodprecio, pfsabprodstock, pfsabprodestado, pfsabprodcreatedat, categoriaid)
            db.session.add(newcateprod)
            db.session.commit()
            flash('Guardado Correctamente', category='success')
            return redirect(url_for('adcapr.controllerAdminCateProdList'))
        else:
            flash('LLene los campos completos porfabor', category='success')
            return redirect(url_for('adcapr.controllerAdminCateProdList'))

    def onGetControllerAdminCateProdUpdate(id):
        productos = Producto.query.get(id)
        categorias = Categoria.query.all()
        if request.method == 'POST':
            productos.pfsabprodnombre = request.form['txtNombre']
            productos.pfsabprodimage = request.form['txtImage']
            productos.pfsabproddetalle = request.form['txtDetalle']
            productos.pfsabprodprecio = request.form['txtPrecio']
            productos.pfsabprodstock = request.form['txtStock']
            productos.pfsabprodestado = request.form['selectEstado']
            productos.pfsabprodcreatedat = datetime.now().strftime('%x')
            productos.categoriaid = request.form['selectCategoria']
            if productos.pfsabprodnombre != '' and productos.pfsabprodimage != '' and productos.pfsabproddetalle != '' and productos.pfsabprodprecio != '' and productos.pfsabprodstock != '' and productos.pfsabprodestado != 'Elija...' and productos.pfsabprodcreatedat != '' and productos.categoriaid != 'Elija...':
                db.session.commit()
                flash('Datos Actualizados', category='success')
                return redirect(url_for('adcapr.controllerAdminCateProdList'))
            else:
                flash('Campos vacios llene porfabor', category='success')
                return redirect(url_for('adcapr.controllerAdminCateProdList'))
        return render("modal/modalAdminCateProdUpdate.html", productos=productos, categorias=categorias)

    def onGetControllerAdminCateProdDelete(id):
        caso = Producto.query.get(id)
        if caso.id >= 0:
            db.session.delete(caso)
            db.session.commit()
            flash('Categoria eliminada', category='danger')
            return redirect(url_for('adcaca.controllerAdminCateCasoList'))
        else:
            flash('Error en el servidor', category='danger')
            return redirect(url_for('adcaca.controllerAdminCateCasoList'))
