from flask_login import UserMixin
from app.auth.auth import Auth
class UserModel(UserMixin):
    def __init__(self, userData):
        self.id = userData.pfsabusername
        self.iduser = userData.pfsabid
        self.password = userData.pfsabpassword
        self.email = userData.pfsabemail
        self.avatar = userData.pfsabavatar
        self.isadmin = userData.pfsabisadmin
        self.estado = userData.pfsabestado
        
    @staticmethod
    def get(username):
        userData = Auth.getUserByUsername(username)
        return UserModel(userData)