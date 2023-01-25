from flask import Blueprint
from app.controllers.controllerAdminPromociones import ControllerAdminPromociones
# admin - categoria - caso
adpromo= Blueprint('adpromo', __name__)
adpromo.route('/adpromo', methods=['GET', 'POST'], defaults={"page": 1})(ControllerAdminPromociones.controllerAdminPromoList)
adpromo.route('/adpromo/<int:page>', methods=['GET', 'POST'])(ControllerAdminPromociones.controllerAdminPromoList)
adpromo.route('/newpp', methods=['POST'])(ControllerAdminPromociones.onGetControllerAdminPromoSave)
adpromo.route('/delcp/<id>', methods=['GET'])(ControllerAdminPromociones.onGetControllerAdminPromoDelete)
adpromo.route('/uppp/<id>', methods=['GET', 'POST'])(ControllerAdminPromociones.onGetControllerAdminPromoUpdate)


