from flask import Flask
from flask_login import LoginManager
from .config.config import Config
from app.database.database import db, ma
from flask_bootstrap import Bootstrap
from flask_fontawesome import FontAwesome
from app.routes.routerAuth import auth
from app.routes.routerLoginIn import loginin
from app.routes.routerLogout import logout
from app.routes.routerDataBase import psfabcdb
from app.routes.routerAdminCategoria import adcate 
from app.routes.routerAdminCateProd import adcapr 
from app.routes.routerAdminPromo import adpromo
from app.routes.routerClientCategoria import clca
from app.routes.routerClientProducto import rcp 
from app.routes.routerClientPromociones import rcpm 
from app.routes.routerClientCarrito import rcct 
from app.routes.routerClientCanasta import rcnt  
from app.routes.routerAdminClients import racl 
from app.routes.routerAdminCanasta import racnt 
from app.routes.routerAdminCanastaPdf import racp 
from app.routes.routerAdminLucro import ralcr 
from app.routes.routerClientQuienesSomos import rcqs
from app.middlewares.authLogin import UserModel

loginManager = LoginManager()
loginManager.loginView = 'auth.authLoginIn'

@loginManager.user_loader
def loadUser(username):
    return UserModel.get(username)

def apprun():
    #Sistem
    app = Flask(__name__)
    app.config.from_object(Config)
    app.register_blueprint(auth)
    app.register_blueprint(psfabcdb)
    app.register_blueprint(loginin)
    app.register_blueprint(logout)
    #Admin
    app.register_blueprint(adcate)
    app.register_blueprint(adcapr)
    app.register_blueprint(adpromo)
    app.register_blueprint(racl)
    app.register_blueprint(racnt)
    app.register_blueprint(racp)
    app.register_blueprint(ralcr)
    # Client
    app.register_blueprint(clca)
    app.register_blueprint(rcp)
    app.register_blueprint(rcpm)
    app.register_blueprint(rcct)
    app.register_blueprint(rcnt)
    app.register_blueprint(rcqs)

    
    #Sistem
    loginManager.init_app(app)
    db.init_app(app)
    ma.init_app(app)
    bootstrap = Bootstrap(app)
    fa = FontAwesome(app)
    return app



