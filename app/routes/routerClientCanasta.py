from flask import Blueprint
from app.controllers.controllerClientCanasta import ControllerClientCanasta
rcnt= Blueprint('rcnt', __name__)
rcnt.route('/rcnt', methods=['GET'])(ControllerClientCanasta.onGetControllerClientCanastaList)
rcnt.route('/rcup/<dpid>/<dpcant>/<pid>', methods=['GET'])(ControllerClientCanasta.onGetControllerClientProductUpdate)
rcnt.route('/rcsv', methods=['POST'])(ControllerClientCanasta.onGetControllerClientSaveCanasta)


