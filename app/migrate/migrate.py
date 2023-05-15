import sys
from datetime import datetime
from app.database.database import *
def createDB():
    db.drop_all()
    db.create_all()

def initDB():
    createDB()
    admin = User(
        pfsabcedula = "1725302705",
        pfsabnombres = "edgar fabian",
        pfsabapellidos = "estrella guambuguete",
        pfsabusername = "starfaby",
        pfsabemail = "star._faby@hotmail.com",
        pfsabpassword = "star123",
        pfsabdireccion = "Ferroviaria Media Adrian Navarro S11-82 y puna", 
        pfsabcellphone = "0983856136", 
        pfsabphone = "022647002", 
        pfsabisadmin = True,
        pfsabavatar = "https://res.cloudinary.com/dqmbrjl7jfs/image/upload/v1638923678/starfaby_uqbwru.jpg",
        pfsabestado = 1,
        pfsabcreatedat = datetime.now()
           
    )
    admin.onGetSetPassword(admin.pfsabpassword)
    db.session.add(admin)
    db.session.commit()  
    return 'base de datos creado existosamente'  