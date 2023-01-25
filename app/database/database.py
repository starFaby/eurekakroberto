from msilib import sequence
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

db = SQLAlchemy()
ma = Marshmallow()

#---------------------------
#drop database flaskmysql
#create database flaskmysql
#---------------------------

#----------------------------
#----------usuario----------
#--------------------------
class User(db.Model):
    __tablename__='pfsabusers'

    pfsabid = db.Column(db.Integer, primary_key=True)
    pfsabcedula = db.Column(db.String(80), nullable=False)
    pfsabnombres = db.Column(db.String(80), nullable=False)
    pfsabapellidos = db.Column(db.String(80), nullable=False)
    pfsabusername = db.Column(db.String(30), unique=True, nullable=False)
    pfsabemail = db.Column(db.String(120), nullable=False)
    pfsabpassword = db.Column(db.String(250), nullable=True)
    pfsabcellphone = db.Column(db.String(25), nullable=False)
    pfsabphone = db.Column(db.String(20), nullable=False)
    pfsabisadmin = db.Column(db.Boolean, default=False)
    pfsabavatar = db.Column(db.String(250), nullable=True)
    pfsabestado = db.Column(db.String(1), nullable=True)
    pfsabcreatedat = db.Column(db.String(11), nullable=True) 

    def onGetSetPassword(self, pfsabpassword):
        self.pfsabpassword = generate_password_hash(pfsabpassword)

    def onGetCheckPassword(self, pfsabpassword):
        return check_password_hash(self.pfsabpassword, pfsabpassword)

    def __init__(self, pfsabcedula, pfsabnombres, pfsabapellidos, pfsabusername, pfsabemail, pfsabpassword, pfsabcellphone, pfsabphone, pfsabisadmin, pfsabavatar, pfsabestado, pfsabcreatedat):
        self.pfsabcedula = pfsabcedula
        self.pfsabnombres = pfsabnombres
        self.pfsabapellidos = pfsabapellidos
        self.pfsabusername = pfsabusername
        self.pfsabemail = pfsabemail
        self.pfsabpassword = pfsabpassword
        self.pfsabcellphone = pfsabcellphone
        self.pfsabphone = pfsabphone
        self.pfsabisadmin = pfsabisadmin
        self.pfsabavatar = pfsabavatar
        self.pfsabestado = pfsabestado
        self.pfsabcreatedat = pfsabcreatedat

class UserSchema(ma.Schema):
    class Meta:
        fields = ('pfsabid','pfsabcedula', 'pfsabnombres', 'pfsabapellidos', 'pfsabusername', 'pfsabemail', 'pfsabpassword', 'pfsabcellphone','pfsabphone', 'pfsabisadmin', 'pfsabavatar', 'pfsabestado', 'pfsabcreatedat')

userSchema = UserSchema()
usersSchema = UserSchema(many=True)

#----------------------------
#----------CATEGORIA----------
#--------------------------
class Categoria(db.Model):
    __tablename__='pfsabcategorias'

    pfsabcateid = db.Column(db.Integer, primary_key=True)
    pfsabcatenombre = db.Column(db.String(80), nullable=False)
    pfsabcateimage = db.Column(db.String(300), nullable=False)
    pfsabcatedetalle = db.Column(db.String(300), nullable=False)
    pfsabcateestado = db.Column(db.String(1), nullable=True)
    pfsabcatecreatedat = db.Column(db.String(11), nullable=True) 


    def __init__(self, pfsabcatenombre, pfsabcateimage, pfsabcatedetalle , pfsabcateestado, pfsabcatecreatedat):
        self.pfsabcatenombre = pfsabcatenombre
        self.pfsabcateimage = pfsabcateimage
        self.pfsabcatedetalle = pfsabcatedetalle
        self.pfsabcateestado = pfsabcateestado
        self.pfsabcatecreatedat = pfsabcatecreatedat

class CategoriaSchema(ma.Schema):
    class Meta:
        fields = ('pfsabcateid','pfsabcatenombre', 'pfsabcateimage', 'pfsabcatedetalle', 'pfsabcateestado', 'pfsabcatecreatedat')

categoriaSchema = CategoriaSchema()
categoriaSchema = CategoriaSchema(many=True)

#----------------------------
#----------PRODUCTO----------
#--------------------------
class Producto(db.Model):
    __tablename__='pfsabproductos'

    pfsabprodid = db.Column(db.Integer, primary_key=True)
    pfsabprodnombre = db.Column(db.String(80), nullable=False)
    pfsabprodimage = db.Column(db.String(300), nullable=False)
    pfsabproddetalle = db.Column(db.String(300), nullable=False)
    pfsabprodprecio = db.Column(db.String(6), nullable=False) #double
    pfsabprodstock = db.Column(db.String(10), nullable=False) #int
    pfsabprodestado = db.Column(db.String(1), nullable=True)
    pfsabprodcreatedat = db.Column(db.String(11), nullable=True) 
    pfsabcategoriaid = db.Column(db.Integer, db.ForeignKey('pfsabcategorias.pfsabcateid',ondelete='CASCADE'), nullable=False)
    pfsabcategoria = db.relationship('Categoria',backref=db.backref('pfsabproductos',lazy=True))


    def __init__(self, pfsabprodnombre, pfsabprodimage, pfsabproddetalle, pfsabprodprecio, pfsabprodstock, pfsabprodestado, pfsabprodcreatedat, pfsabcategoriaid):
        self.pfsabprodnombre = pfsabprodnombre
        self.pfsabprodimage = pfsabprodimage
        self.pfsabproddetalle = pfsabproddetalle
        self.pfsabprodprecio = pfsabprodprecio
        self.pfsabprodstock = pfsabprodstock
        self.pfsabprodestado = pfsabprodestado
        self.pfsabprodcreatedat = pfsabprodcreatedat
        self.pfsabcategoriaid = pfsabcategoriaid
class ProductoSchema(ma.Schema):
    class Meta:
        fields = ('pfsabprodid','pfsabprodnombre', 'pfsabprodimage', 'pfsabproddetalle', 'pfsabprodprecio', 'pfsabprodstock', 'pfsabprodestado', 'pfsabprodcreatedat','pfsabcategoriaid')

productoSchema = ProductoSchema()
productoSchema = ProductoSchema(many=True)


#----------------------------
#----------Promociones----------
#--------------------------
class Promociones(db.Model):
    __tablename__='pfsabpromociones'

    pfsabpromid = db.Column(db.Integer, primary_key=True)
    pfsabpromdto = db.Column(db.String(80), nullable=False)
    pfsabpromfechainicio = db.Column(db.String(10), nullable=False)
    pfsabpromfechafin = db.Column(db.String(10), nullable=False)
    pfsabpromdescripcion = db.Column(db.String(300), nullable=False) #double
    pfsabpromestado = db.Column(db.String(1), nullable=True)
    pfsabpromcreatedat = db.Column(db.String(11), nullable=True) 

    pfsabproductoid = db.Column(db.Integer, db.ForeignKey('pfsabproductos.pfsabprodid',ondelete='CASCADE'), nullable=False)
    pfsabproducto = db.relationship('Producto',backref=db.backref('pfsabpromociones',lazy=True))


    def __init__(self, pfsabpromdto, pfsabpromfechainicio, pfsabpromfechafin, pfsabpromdescripcion, pfsabpromestado, pfsabpromcreatedat, pfsabproductoid):
        self.pfsabpromdto = pfsabpromdto
        self.pfsabpromfechainicio = pfsabpromfechainicio
        self.pfsabpromfechafin = pfsabpromfechafin
        self.pfsabpromdescripcion = pfsabpromdescripcion
        self.pfsabpromestado = pfsabpromestado
        self.pfsabpromcreatedat = pfsabpromcreatedat 
        self.pfsabproductoid = pfsabproductoid 

class PromocionSchema(ma.Schema):
    class Meta:
        fields = ('pfsabpromid','pfsabpromdto', 'pfsabpromfechainicio', 'pfsabpromfechafin', 'pfsabpromdescripcion', 'pfsabpromestado', 'pfsabpromcreatedat','pfsabpromocionid')

promocionSchema = PromocionSchema()
promocionSchema = PromocionSchema(many=True)

