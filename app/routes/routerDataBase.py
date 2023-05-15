from flask import Blueprint
from app.migrate.migrate import initDB

psfabcdb= Blueprint('psfabcdb', __name__)

psfabcdb.route('/psfabcdb', methods=['GET'])(initDB)
