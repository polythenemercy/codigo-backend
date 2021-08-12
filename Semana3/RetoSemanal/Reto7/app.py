#Procedimiento - Importar referencias:
from flask import Flask
from flask import request
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_marshmallow import fields
import json

#Procedimiento - Instanciación de referencia:
app = Flask(__name__)

#Procedimiento - Instanciación de parametro:
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://codigotecsup:codigotecsup@144.91.114.93/codigo_tecsup"

#Procedimiento - Instanciación:
db = SQLAlchemy(app)
ma = Marshmallow(app)

#Procedimiento - Creación de clase:
class Datainfo(db.Model):
  IdReg = db.Column(db.String(250))
  DataValue = db.Column(db.Integer, primary_key = True)
  DateRegister = db.Column(db.Date)

class DatainfoSchema(ma.Schema):
  class Meta:
    fields = ["IdReg", "DataValue"]

@app.route('/')
def list_data():
  dataset = Datainfo.query.all()
  schema = DatainfoSchema()
  data = schema.dump(dataset, many=True)
  response = {
    "status": "ok",
    "content": data
  }
  return json.dumps(response)

@app.route('/create', methods=['POST'])
def create_data():
    data = request.json
    sql1 = f"INSERT INTO datainfo (DataValue) VALUES ('{data['DataValue']}');"
    result = db.engine.execute(sql1)
    return 'OK' , 201