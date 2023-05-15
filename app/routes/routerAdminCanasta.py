from flask import Blueprint
from app.controllers.controllerAdminCanasta import ControllerAdminCanasta
# admin - categoria - caso
racnt= Blueprint('racnt', __name__)
racnt.route('/racnt', methods=['GET', 'POST'], defaults={"page": 1})(ControllerAdminCanasta.onGetControllerAdminCanastaList)
racnt.route('/racnt/<int:page>', methods=['GET', 'POST'])(ControllerAdminCanasta.onGetControllerAdminCanastaList)

