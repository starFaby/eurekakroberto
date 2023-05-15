from flask import Blueprint
from app.controllers.controllerAdminClient import ControllerClients
# admin - categoria - caso
racl= Blueprint('racl', __name__)
racl.route('/racl', methods=['GET', 'POST'], defaults={"page": 1})(ControllerClients.onGetControllerClientsList)
racl.route('/racl/<int:page>', methods=['GET', 'POST'])(ControllerClients.onGetControllerClientsList)

