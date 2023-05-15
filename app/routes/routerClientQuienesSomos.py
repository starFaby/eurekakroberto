from flask import Blueprint
from app.controllers.controllerClientQuienesSomos import ControllerClientQuienesSomos
rcqs= Blueprint('rcqs', __name__)
rcqs.route('/rcqs', methods=['GET'])(ControllerClientQuienesSomos.onGetControllerClientQuienesSomos)

