#Procedimiento - Importar referencias:
from flask import Flask
from flask import render_template
from flask_sqlalchemy import SQLAlchemy

#Procedimiento - Instanciación de referencia:
app = Flask(__name__)

#Procedimiento - Instanciación de parametro:
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://codigotecsup:codigotecsup@144.91.114.93/codigo_tecsup"

#Procedimiento - Instanciación:
db = SQLAlchemy(app)

#Procedimiento - Importar referencias:
from models import Datainfo

@app.route('/data')
def get_data():
  dataset = Datainfo.query.all()
  return render_template("index.html", dataset = dataset)