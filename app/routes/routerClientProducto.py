from flask import Blueprint
from app.controllers.controllerClientProducto import ControllerClientProducto
rcp= Blueprint('rcp', __name__)
rcp.route('/rcp/<id>', methods=['GET'])(ControllerClientProducto.onGetControllerProductoList)
#caso.route('/newcs', methods=['POST'])(ControllerClientProducto.onGetcontrollerCasoInsert) 