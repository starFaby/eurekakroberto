from flask import Blueprint
from app.controllers.controllerAdminCanastaPdf import ControllerAdminCanastaPdf
# admin - categoria - caso
racp= Blueprint('racp', __name__)
racp.route('/racp/<int:user>/<int:cnst>', methods=['GET', 'POST'])(ControllerAdminCanastaPdf.onGetControllerAdminCanastaPdf)
