from flask import Blueprint
from app.controllers.controllerClientCarrito import ControllerClientCarrito
rcct= Blueprint('rcct', __name__)
rcct.route('/rcct/<id>', methods=['GET'])(ControllerClientCarrito.onGetControllerClientCarritoList)

