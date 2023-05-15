from flask import request, render_template as render, flash
from app.database.database import *
from sqlalchemy.exc import SQLAlchemyError
from flask import g

class ControllerAdminCanasta:

    def onGetControllerAdminCanastaList(page):
        page = page
        pages = 5
        try:
            canastaUser = Proforma.query.join(User, Proforma.pfsabuserid == User.pfsabid).add_columns( User.pfsabid,User.pfsabcedula, User.pfsabnombres, User.pfsabapellidos,Proforma.pfsabpfid, Proforma.pfsabpfnumpf, Proforma.pfsabpftotal, Proforma.pfsabpfcreatedat).order_by(Proforma.pfsabpfid.asc()).paginate(page=page, per_page=pages ,error_out=False)
            if canastaUser != []:
                if request.method == 'POST' and 'tag' in request.form:
                    tag = request.form["tag"]
                    search = "%{}%".format(tag)
                    canastaUser = Proforma.query.join(User, Proforma.pfsabuserid == User.pfsabid).add_columns( User.pfsabid,User.pfsabcedula, User.pfsabnombres, User.pfsabapellidos,Proforma.pfsabpfid, Proforma.pfsabpfnumpf, Proforma.pfsabpftotal, Proforma.pfsabpfcreatedat).order_by(Proforma.pfsabpfid.asc()).filter(User.pfsabcedula.like(search)).paginate(per_page=pages,error_out=False)
                    return render("admin/adminCanasta.html", canastaUser=canastaUser, tag = tag)
                else:    
                    flash('Producto Listadas', category='success')
                    return render("admin/adminCanasta.html", canastaUser=canastaUser)
            else:
                flash('No existe categorias', category='success')
                return render("admin/adminCanasta.html", canastaUser=canastaUser)
        except SQLAlchemyError as e:
            error = str(e.__dict__['orig'])
            print(error)
            return render('errors/error500.html')
