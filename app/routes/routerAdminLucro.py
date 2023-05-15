from flask import Blueprint
from app.controllers.controllerAdminLucro import ControllerAdminLucro
# admin - categoria - caso
ralcr= Blueprint('ralcr', __name__)
ralcr.route('/ralcr', methods=['GET'])(ControllerAdminLucro.onGetControllerLucroList)
ralcr.route('/ralsave', methods=['POST'])(ControllerAdminLucro.onGetControllerLucroSave)

