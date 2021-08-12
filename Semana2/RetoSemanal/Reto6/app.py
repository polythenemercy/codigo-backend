#Procedimiento - Importar referencias:
from flask import Flask
from flask import request

#Procedimiento - Instanciación de referencia:
app = Flask(__name__)

#Declaración de variables:
tasks = {
}

#Procedimiento - Creación de ruta:
@app.route('/get_task')
def getData():
  return tasks

#Procedimiento - Creación de ruta:
@app.route('/create_task', methods=['POST'])
def createData():
  data = request.json
  tasks[data["id"]] = {
    "priority": data["priority"],
    "description": data["description"]
  }
  return "ok", 201

#Procedimiento - Creación de ruta:
@app.route('/delete_task', methods=['DELETE'])
def deleteData():
  id = request.args.get('id')
  tasks.pop(id)
  return "ok", 204

#Procedimiento - Creación de ruta:
@app.route('/update_task', methods=['PUT'])
def updateData():
  id = request.args.get('id')
  data = request.json
  updated_task = tasks.get(id)
  updated_task.update(data)
  tasks[id] = updated_task
  return "ok"

