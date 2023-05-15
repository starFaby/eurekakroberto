from flask import Blueprint
from app.controllers.controllerAdminCategoria import ControllerAdminCategoria
adcate= Blueprint('adcate', __name__)
adcate.route('/adcate', methods=['GET', 'POST'], defaults={"page": 1})(ControllerAdminCategoria.controllerAdminCategoriaList)
adcate.route('/adcate/<int:page>', methods=['GET', 'POST'])(ControllerAdminCategoria.controllerAdminCategoriaList)
adcate.route('/new', methods=['POST'])(ControllerAdminCategoria.onGetControllerAdminCategoriaSave)
adcate.route('/delcate/<id>', methods=['GET'])(ControllerAdminCategoria.onGetControllerAdminCategoriaDelete)
adcate.route('/updcate/<id>', methods=['GET', 'POST'])(ControllerAdminCategoria.onGetControllerAdminCategoriaUpdate)

