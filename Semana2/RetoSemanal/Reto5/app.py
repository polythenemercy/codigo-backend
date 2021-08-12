#Procedimiento - Importar referencias:
from flask import Flask
from flask import request

#Procedimiento - Instanciación de referencia:
app = Flask(__name__)

#Declaración de variables:
data = {
  "d01": {
    "description": "Initial value #1"
  }
}

#Procedimiento - Creación de ruta:
@app.route('/')
def getData():
  return data

#Procedimiento - Creación de ruta:
@app.route('/new_data', methods=['POST'])
def createData():
  post_data = request.json
  data[post_data["id"]] = {
    "description": post_data["description"]
  }
  return "ok", 201
