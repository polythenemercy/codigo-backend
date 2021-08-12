#Procedimiento - Importar referencias:
from flask import Flask

#Procedimiento - Instanciación de referencia:
app = Flask(__name__)

#Declaración de variable:
data = {
  "ok": True,
  "content": [
    "AMAZONAS",
    "ANCASH",
    "APURIMAC",
    "AREQUIPA",
    "AYACUCHO",
    "CAJAMARCA",
    "CALLAO",
    "CUSCO",
    "HUANCAVELICA",
    "HUANUCO",
    "COLOMBIA",
    "ICA",
    "JUNIN",
    "LA LIBERTAD",
    "LAMBAYEQUE",
    "LIMA",
    "LORETO",
    "MADRE DE DIOS",
    "MOQUEGUA",
    "PASCO",
    "PIURA",
    "PUNO",
    "SAN MARTIN",
    "TACNA",
    "TUMBES",
    "UCAYALI"    
  ],
  "message": "Data succesfully retrieved"
}

#Procedimiento - Creación de ruta:
@app.route('/')
def get_index():
  return {
    "ok": "Hello world"
  }
  
#Procedimiento - Creación de ruta:
@app.route('/get_dpto')
def get_dpto():
  return data