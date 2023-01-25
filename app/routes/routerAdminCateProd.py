from flask import Blueprint
from app.controllers.controllerAdminCateProd import ControllerAdminCateProd
# admin - categoria - caso
adcapr= Blueprint('adcapr', __name__)
adcapr.route('/adcapr', methods=['GET', 'POST'], defaults={"page": 1})(ControllerAdminCateProd.controllerAdminCateProdList)
adcapr.route('/adcapr/<int:page>', methods=['GET', 'POST'])(ControllerAdminCateProd.controllerAdminCateProdList)
adcapr.route('/newcp', methods=['POST'])(ControllerAdminCateProd.onGetControllerAdminCateProdSave)
adcapr.route('/delcp/<id>', methods=['GET'])(ControllerAdminCateProd.onGetControllerAdminCateProdDelete)
adcapr.route('/upcp/<id>', methods=['GET', 'POST'])(ControllerAdminCateProd.onGetControllerAdminCateProdUpdate)

