from datetime import datetime
from flask import request, render_template as render, flash, redirect, url_for
from app.database.database import *


class ControllerAdminPromociones:

    def controllerAdminPromoList(page):
        page = page
        pages = 5
        promoProd = Promociones.query.order_by(Promociones.pfsabpromid.asc()).paginate(page, pages,error_out=False)
        productos = Producto.query.all()
        if promoProd != [] or productos != []:
            if request.method == 'POST' and 'tag' in request.form:
                tag = request.form["tag"]
                search = "%{}%".format(tag)
                promoProd = Promociones.query.filter(Promociones.pfsabpromdescripcion.like(search)).paginate(per_page=pages,error_out=False)
                return render("admin/adminPromociones.html", promoProd=promoProd, productos=productos, tag = tag)
            else:    
                flash('Promociones Listadas', category='success')
                return render("admin/adminPromociones.html", promoProd=promoProd, productos=productos)
        else:
            flash('No existe Promociones', category='success')
            return render("admin/adminPromociones.html", promoProd=promoProd, productos=productos)

    def onGetControllerAdminPromoSave():
        pfsabpromdto = request.form['txtDto']
        pfsabpromfechainicio = request.form['txtFechaInicio']
        pfsabpromfechafin = request.form['txtFechaFin']
        pfsabpromdescripcion = request.form['txtDescripcion']
        pfsabpromestado = request.form['selectEstado']
        pfsabpromcreatedat = datetime.now().strftime('%x')
        pfsabproductoid = request.form['selectCategoria']
        if pfsabpromdto != '' and pfsabpromfechainicio != '' and pfsabpromfechafin != ''and pfsabpromdescripcion != '' and pfsabpromestado != 'Elija...' and pfsabpromcreatedat != '' and pfsabproductoid != 'Elija...':
            newpromoprod = Promociones(pfsabpromdto, pfsabpromfechainicio, pfsabpromfechafin,pfsabpromdescripcion, pfsabpromestado, pfsabpromcreatedat, pfsabproductoid)
            db.session.add(newpromoprod)
            db.session.commit()
            flash('Guardado Correctamente', category='success')
            return redirect(url_for('adpromo.controllerAdminPromoList'))
        else:
            flash('LLene los campos completos porfabor', category='success')
            return redirect(url_for('adpromo.controllerAdminPromoList'))

    def onGetControllerAdminPromoUpdate(id):
        promocion = Promociones.query.get(id)
        productos = Producto.query.all()
        if request.method == 'POST':
            promocion.pfsabpromdto = request.form['txtDto']
            promocion.pfsabpromfechainicio = request.form['txtFechaInicio']
            promocion.pfsabpromfechafin = request.form['txtFechaFin']
            promocion.pfsabpromdescripcion = request.form['txtDescripcion']
            promocion.pfsabpromestado = request.form['selectEstado']
            promocion.pfsabpromcreatedat = datetime.now().strftime('%x')
            promocion.pfsabproductoid = request.form['selectCategoria']
            if promocion.pfsabpromdto != '' and promocion.pfsabpromfechainicio != '' and promocion.pfsabpromfechafin != '' and promocion.pfsabpromdescripcion != '' and promocion.pfsabpromestado != 'Elija...' and promocion.pfsabpromcreatedat != '' and promocion.pfsabproductoid != 'Elija...':
                db.session.commit()
                flash('Datos Actualizados', category='success')
                return redirect(url_for('adpromo.controllerAdminPromoList'))
            else:
                flash('Campos vacios llene porfabor', category='success')
                return render("modal/modalAdminPromoUpdate.html")

        return render("modal/modalAdminPromoUpdate.html", promocion=promocion, productos=productos)

    def onGetControllerAdminPromoDelete(id):
        promocion = Promociones.query.get(id)
        if promocion.id >= 0:
            db.session.delete(promocion)
            db.session.commit()
            flash('Promocion eliminada', category='info')
            return redirect(url_for('adpromo.controllerAdminPromoList'))
        else:
            flash('Error en el servidor', category='danger')
            return redirect(url_for('adpromo.controllerAdminPromoList'))
