#Procedimiento - Importar referencias:
from app import db

#Procedimiento - Creación de clase:
class Datainfo(db.Model):
  IdReg = db.Column(db.String(250))
  DataValue = db.Column(db.Integer, primary_key = True)
  DateRegister = db.Column(db.Date)

