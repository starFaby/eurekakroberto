from flask import Blueprint
from app.controllers.controllerClientCategoria import ControllerClientCategoria
clca= Blueprint('clca', __name__)
clca.route('/clca', methods=['GET'])(ControllerClientCategoria.onGetControllerClientCategoriaList)
