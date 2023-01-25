from flask import Blueprint
from app.controllers.controllerClientPromociones import ControllerClientPromociones
rcpm= Blueprint('rcpm', __name__)
rcpm.route('/rcpm', methods=['GET'])(ControllerClientPromociones.onGetControllerClientPromocionesList)
#caso.route('/newcs', methods=['POST'])(ControllerClientProducto.onGetcontrollerCasoInsert) 