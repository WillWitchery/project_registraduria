from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS
import json
from waitress import serve
from Controladores.ControladorUser import ControladorUser

app=Flask(__name__)
cors = CORS(app)
miControladorUsuario=ControladorUser()

def loadFileConfig():
    with open('config.json') as f:
        data = json.load(f)
    return data

@app.route("/",methods=['GET'])
def test():
    json = {}
    json["message"]="Server running ..."
    return jsonify(json)

#_________metodos estudiantes___________
@app.route("/user",methods=['GET'])
def getUser():
    json=miControladorUsuario.index()
    return jsonify(json)

@app.route("/user",methods=['POST'])
def crearUsuario():
    data = request.get_json()
    json=miControladorUsuario.create(data)
    return jsonify(json)

@app.route("/user/<string:id>",methods=['GET'])
def getUsuario(id):
    json=miControladorUsuario.show(id)
    return jsonify(json)

@app.route("/user/<string:id>",methods=['PUT'])
def modificarUsuario(id):
    data = request.get_json()
    json=miControladorUsuario.update(id,data)
    return jsonify(json)

@app.route("/user/<string:id>",methods=['DELETE'])
def eliminarUsuario(id):
    json=miControladorUsuario.delete(id)
    return jsonify(json)

if __name__=='__main__':
    dataConfig = loadFileConfig()
    print("Server running : "+"http://"+dataConfig["url-backend"]+":" + str(dataConfig["port"]))
    serve(app,host=dataConfig["url-backend"],port=dataConfig["port"])


