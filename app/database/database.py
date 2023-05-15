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
    pfsabdireccion = db.Column(db.String(100), nullable=True)
    pfsabcellphone = db.Column(db.String(25), nullable=False)
    pfsabphone = db.Column(db.String(20), nullable=False)
    pfsabisadmin = db.Column(db.Boolean, default=False)
    pfsabavatar = db.Column(db.String(250), nullable=True)
    pfsabestado = db.Column(db.String(1), nullable=True)
    pfsabcreatedat = db.Column(db.Date, nullable=True) 

    def onGetSetPassword(self, pfsabpassword):
        self.pfsabpassword = generate_password_hash(pfsabpassword)

    def onGetCheckPassword(self, pfsabpassword):
        return check_password_hash(self.pfsabpassword, pfsabpassword)

    def __init__(self, pfsabcedula, pfsabnombres, pfsabapellidos, pfsabusername, pfsabemail, pfsabpassword, pfsabdireccion,  pfsabcellphone, pfsabphone, pfsabisadmin, pfsabavatar, pfsabestado, pfsabcreatedat):
        self.pfsabcedula = pfsabcedula
        self.pfsabnombres = pfsabnombres
        self.pfsabapellidos = pfsabapellidos
        self.pfsabusername = pfsabusername
        self.pfsabemail = pfsabemail
        self.pfsabpassword = pfsabpassword 
        self.pfsabdireccion = pfsabdireccion 
        self.pfsabcellphone = pfsabcellphone
        self.pfsabphone = pfsabphone
        self.pfsabisadmin = pfsabisadmin
        self.pfsabavatar = pfsabavatar
        self.pfsabestado = pfsabestado
        self.pfsabcreatedat = pfsabcreatedat

class UserSchema(ma.Schema):
    class Meta:
        fields = ('pfsabid','pfsabcedula', 'pfsabnombres', 'pfsabapellidos', 'pfsabusername', 'pfsabemail', 'pfsabpassword', 'pfsabdireccion', 'pfsabcellphone','pfsabphone', 'pfsabisadmin', 'pfsabavatar', 'pfsabestado', 'pfsabcreatedat')

userSchema = UserSchema()
usersSchema = UserSchema(many=True)

#----------------------------
#----------PROFORMA----------
#--------------------------

class Proforma(db.Model):
    __tablename__='pfsabproforma'

    pfsabpfid = db.Column(db.Integer, primary_key=True)
    pfsabpfnumpf = db.Column(db.Integer, nullable=False)
    pfsabpfsubtotal = db.Column(db.Integer, nullable=False)
    pfsabpfdto = db.Column(db.Integer, nullable=False)
    pfsabpfiva = db.Column(db.Integer, nullable=False)
    pfsabpftotal = db.Column(db.Integer, nullable=False)
    pfsabpfestado = db.Column(db.String(1), nullable=True)
    pfsabpfcreatedat = db.Column(db.Date, nullable=True) 

    pfsabuserid = db.Column(db.Integer, db.ForeignKey('pfsabusers.pfsabid',ondelete='CASCADE'), nullable=False)
    pfsabuser = db.relationship('User',backref=db.backref('pfsabproforma',lazy=True))



    def __init__(self, pfsabpfnumpf, pfsabpfsubtotal, pfsabpfdto, pfsabpfiva, pfsabpftotal, pfsabpfestado, pfsabpfcreatedat, pfsabuserid):
        self.pfsabpfnumpf = pfsabpfnumpf
        self.pfsabpfsubtotal = pfsabpfsubtotal
        self.pfsabpfdto = pfsabpfdto
        self.pfsabpfiva = pfsabpfiva
        self.pfsabpftotal = pfsabpftotal
        self.pfsabpfestado = pfsabpfestado
        self.pfsabpfcreatedat = pfsabpfcreatedat 
        self.pfsabuserid = pfsabuserid 

class ProformaSchema(ma.Schema):
    class Meta:
        fields = ('pfsabpfid', 'pfsabpfnumpf', 'pfsabpfsubtotal', 'pfsabpfdto', 'pfsabpfiva', 'pfsabpftotal', 'pfsabpfestado', 'pfsabpfcreatedat', 'pfsabuserid')

proformaSchema = ProformaSchema()
proformaSchema = ProformaSchema(many=True)


#----------------------------
#----------DETALLE PROFORMA----------
#--------------------------

class Detalleproforma(db.Model):
    __tablename__='pfsabdetalleproforma'

    pfsabdpid = db.Column(db.Integer, primary_key=True)
    pfsabdpnumpf = db.Column(db.Integer, nullable=False)
    pfsabdpcantidad = db.Column(db.Integer, nullable=False)
    pfsabdprecio = db.Column(db.Integer, nullable=False)
    pfsabdptotal = db.Column(db.Integer, nullable=False)
    pfsabdpestado = db.Column(db.String(1), nullable=True)
    pfsabdpcreatedat = db.Column(db.String(11), nullable=True) 

    pfsabproductoid = db.Column(db.Integer, db.ForeignKey('pfsabproductos.pfsabprodid',ondelete='CASCADE'), nullable=False)
    pfsabproducto = db.relationship('Producto',backref=db.backref('pfsabdetalleproforma',lazy=True))

    pfsabproformaid = db.Column(db.Integer, db.ForeignKey('pfsabproforma.pfsabpfid',ondelete='CASCADE'), nullable=False)
    pfsabproforma = db.relationship('Proforma',backref=db.backref('pfsabdetalleproforma',lazy=True))



    def __init__(self, pfsabdpnumpf, pfsabdpcantidad, pfsabdprecio, pfsabdptotal, pfsabdpestado, pfsabdpcreatedat, pfsabproductoid, pfsabproformaid ):
        self.pfsabdpnumpf = pfsabdpnumpf
        self.pfsabdpcantidad = pfsabdpcantidad
        self.pfsabdprecio = pfsabdprecio
        self.pfsabdptotal = pfsabdptotal
        self.pfsabdpestado = pfsabdpestado
        self.pfsabdpcreatedat = pfsabdpcreatedat
        self.pfsabproductoid = pfsabproductoid
        self.pfsabproformaid = pfsabproformaid

class DetalleproformaSchema(ma.Schema):
    class Meta:
        fields = ('pfsabdpid','pfsabdpnumpf', 'pfsabdpcantidad', 'pfsabdprecio', 'pfsabdptotal', 'pfsabdpestado', 'pfsabdpcreatedat', 'pfsabproductoid', 'pfsabproformaid')

detalleproformaSchema = DetalleproformaSchema()
detalleproformaSchema = DetalleproformaSchema(many=True)

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


#---------------------------------
#----------Forma de Pago----------
#---------------------------------

class Formapago(db.Model):
    __tablename__='pfsabformapago'

    pfsabfpid = db.Column(db.Integer, primary_key=True)
    pfsabfpestado = db.Column(db.String(1), nullable=True)
    pfsabfpcreatedat = db.Column(db.String(11), nullable=True) 

    pfsabproformaid = db.Column(db.Integer, db.ForeignKey('pfsabproforma.pfsabpfid',ondelete='CASCADE'), nullable=False)
    pfsabproforma = db.relationship('Proforma',backref=db.backref('pfsabformapago',lazy=True))

    pfsabtipopagoid = db.Column(db.Integer, db.ForeignKey('pfsabtipopago.pfsabtpid',ondelete='CASCADE'), nullable=False)
    pfsabtipopago = db.relationship('Tipopago',backref=db.backref('pfsabformapago',lazy=True))

    def __init__(self, pfsabfpestado, pfsabfpcreatedat, pfsabproformaid, pfsabtipopagoid):
        self.pfsabfpestado = pfsabfpestado
        self.pfsabfpcreatedat = pfsabfpcreatedat
        self.pfsabproformaid = pfsabproformaid
        self.pfsabtipopagoid = pfsabtipopagoid

class FormapagoSchema(ma.Schema):
    class Meta:
        fields = ('pfsabfpid', 'pfsabfpestado', 'pfsabfpcreatedat', 'pfsabproformaid', 'pfsabtipopagoid')

formapagoSchema = FormapagoSchema()
formapagoSchema = FormapagoSchema(many=True)

#---------------------------------
#----------Tipo de Pago----------
#---------------------------------

class Tipopago(db.Model):
    __tablename__='pfsabtipopago'

    pfsabtpid = db.Column(db.Integer, primary_key=True)
    pfsabtpnombre = db.Column(db.String(30), nullable=True)
    pfsabtpestado = db.Column(db.String(1), nullable=True)
    pfsabtpcreatedat = db.Column(db.String(11), nullable=True) 

    def __init__(self, pfsabtpnombre, pfsabtpestado, pfsabtpcreatedat):
        self.pfsabtpnombre = pfsabtpnombre
        self.pfsabtpestado = pfsabtpestado
        self.pfsabtpcreatedat = pfsabtpcreatedat
 

class TipopagoSchema(ma.Schema):
    class Meta:
        fields = ('pfsabtpid', 'pfsabtpnombre', 'pfsabtpestado', 'pfsabtpcreatedat')

tipopagoSchema = TipopagoSchema()
tipopagoSchema = TipopagoSchema(many=True)


#---------------------------------
#----------Paypal----------
#---------------------------------

class Paypal(db.Model):
    __tablename__='pfsabpaypal'

    pfsabpypid = db.Column(db.Integer, primary_key=True)
    pfsabpypnumproforma = db.Column(db.Integer, nullable=True)
    pfsabpypreproforma = db.Column(db.Integer, nullable=True)
    pfsabpypestado = db.Column(db.String(1), nullable=True)
    pfsabpypcreatedat = db.Column(db.String(11), nullable=True) 


    pfsabformapagoid = db.Column(db.Integer, db.ForeignKey('pfsabformapago.pfsabfpid',ondelete='CASCADE'), nullable=False)
    pfsabformapago = db.relationship('Formapago',backref=db.backref('pfsabpaypal',lazy=True))

    def __init__(self, pfsabpypnumproforma, pfsabpypreproforma, pfsabpypestado, pfsabpypcreatedat, pfsabformapagoid):
        self.pfsabpypnumproforma = pfsabpypnumproforma
        self.pfsabpypreproforma = pfsabpypreproforma
        self.pfsabpypestado = pfsabpypestado
        self.pfsabpypcreatedat = pfsabpypcreatedat
        self.pfsabformapagoid = pfsabformapagoid
 

class PaypalSchema(ma.Schema):
    class Meta:
        fields = ('pfsabpypid', 'pfsabpypnumproforma', 'pfsabpypreproforma', 'pfsabpypestado', 'pfsabpypcreatedat', 'pfsabformapagoid')

paypalSchema = PaypalSchema()
paypalSchema = PaypalSchema(many=True)

#------------------------------------------
#----------Transferencia Bancaria----------
#------------------------------------------

class Transferenciabancaria(db.Model):
    __tablename__='pfsabtransferenciabancaria'

    pfsabtbpid = db.Column(db.Integer, primary_key=True)
    pfsabtbnumproforma = db.Column(db.Integer, nullable=True)
    pfsabtbpreproforma = db.Column(db.Integer, nullable=True)
    pfsabtbboucher = db.Column(db.String(300), nullable=True)
    pfsabtbestado = db.Column(db.String(1), nullable=True)
    pfsabtbcreatedat = db.Column(db.String(11), nullable=True) 


    pfsabformapagoid = db.Column(db.Integer, db.ForeignKey('pfsabformapago.pfsabfpid',ondelete='CASCADE'), nullable=False)
    pfsabformapago = db.relationship('Formapago',backref=db.backref('pfsabtransferenciabancaria',lazy=True))

    def __init__(self, pfsabtbnumproforma, pfsabtbpreproforma, pfsabtbboucher,  pfsabtbestado, pfsabtbcreatedat, pfsabformapagoid):
        self.pfsabtbnumproforma = pfsabtbnumproforma
        self.pfsabtbpreproforma = pfsabtbpreproforma
        self.pfsabtbboucher = pfsabtbboucher
        self.pfsabtbestado = pfsabtbestado
        self.pfsabtbcreatedat = pfsabtbcreatedat
        self.pfsabformapagoid = pfsabformapagoid
 

class TransferenciabancariaSchema(ma.Schema):
    class Meta:
        fields = ('pfsabtbpid', 'pfsabtbnumproforma', 'pfsabtbpreproforma', 'pfsabtbboucher',  'pfsabtbestado', 'pfsabtbcreatedat', 'pfsabformapagoid')

transferenciabancariaSchema = TransferenciabancariaSchema()
transferenciabancariaSchema = TransferenciabancariaSchema(many=True)

#------------------------------------------
#-----------------Efectivo-----------------
#------------------------------------------

class Efectivo(db.Model):
    __tablename__='pfsabefectivo'

    pfsabeftpid = db.Column(db.Integer, primary_key=True)
    pfsabeftnumproforma = db.Column(db.Integer, nullable=True)
    pfsabeftpreproforma = db.Column(db.Integer, nullable=True)
    pfsabeftestado = db.Column(db.String(1), nullable=True)
    pfsabeftcreatedat = db.Column(db.String(11), nullable=True) 


    pfsabformapagoid = db.Column(db.Integer, db.ForeignKey('pfsabformapago.pfsabfpid',ondelete='CASCADE'), nullable=False)
    pfsabformapago = db.relationship('Formapago',backref=db.backref('pfsabefectivo',lazy=True))

    def __init__(self, pfsabeftnumproforma, pfsabeftpreproforma, pfsabeftestado,  pfsabeftcreatedat, pfsabformapagoid):
        self.pfsabeftnumproforma = pfsabeftnumproforma
        self.pfsabeftpreproforma = pfsabeftpreproforma
        self.pfsabeftestado = pfsabeftestado
        self.pfsabeftcreatedat = pfsabeftcreatedat
        self.pfsabformapagoid = pfsabformapagoid
 

class EfectivoSchema(ma.Schema):
    class Meta:
        fields = ('pfsabeftpid', 'pfsabeftnumproforma', 'pfsabeftpreproforma', 'pfsabeftestado',  'pfsabeftcreatedat', 'pfsabformapagoid')

efectivoSchema = EfectivoSchema()
efectivoSchema = EfectivoSchema(many=True)
