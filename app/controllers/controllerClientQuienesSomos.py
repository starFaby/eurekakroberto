from flask import request, render_template as render
from app.database.database import *

class ControllerClientQuienesSomos:

    def onGetControllerClientQuienesSomos():
        return render('client/clientQuienesSomos.html')
 