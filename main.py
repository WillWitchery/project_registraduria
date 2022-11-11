from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS
import json
from waitress import serve
##########################
app = Flask(__name__)
cors = CORS(app)
##########################[[[Imports]]]##########################
from Controladores.ControladorUser import ControladorUser
from Controladores.ControladorCandidatos import ControladorCandidatos
from Controladores.ControladorPartidos import ControladorPartidos
from Controladores.ControladorMesas import ControladorMesas
from Controladores.ControladorResultados import ControladorResultados

miControladorUsuario = ControladorUser()
miControladorCandidatos = ControladorCandidatos()
miControladorPartidos = ControladorPartidos()
miControladorMesas = ControladorMesas()
miControladorResultados = ControladorResultados()
###############################################################
@app.route("/", methods=['GET'])
def test():
    json = {}
    json["message"] = "Server running ..."
    return jsonify(json)

##########################[[[User]]]##########################
@app.route("/user", methods=['GET'])
def getUsuarios():
    json = miControladorUsuario.index()
    return jsonify(json)

@app.route("/user", methods=['POST'])
def crearUsuario():
    data = request.get_json()
    json = miControladorUsuario.create(data)
    return jsonify(json)

@app.route("/user/<string:id>", methods=['GET'])
def getUsuario(id):
    json = miControladorUsuario.show(id)
    return jsonify(json)

@app.route("/user/<string:id>", methods=['PUT'])
def modificarUsuario(id):
    data = request.get_json()
    json = miControladorUsuario.update(id, data)
    return jsonify(json)

@app.route("/user/<string:id>", methods=['DELETE'])
def eliminarUsuario(id):
    json = miControladorUsuario.delete(id)
    return jsonify(json)

##########################[[[Candidatos]]]##########################
@app.route("/candidatos", methods=['GET'])
def getCandidatos():
    json = miControladorCandidatos.index()
    return jsonify(json)

@app.route("/candidatos", methods=['POST'])
def crearCandidato():
    data = request.get_json()
    json = miControladorCandidatos.create(data)
    return jsonify(json)

@app.route("/candidatos/<string:id>", methods=['GET'])
def getCandidato(id):
    json = miControladorCandidatos.show(id)
    return jsonify(json)

@app.route("/candidatos/<string:id>", methods=['PUT'])
def modificarCandidato(id):
    data = request.get_json()
    json = miControladorCandidatos.update(id, data)
    return jsonify(json)

@app.route("/candidatos/<string:id>", methods=['DELETE'])
def eliminarCandidato(id):
    json = miControladorCandidatos.delete(id)
    return jsonify(json)

##########################[[[******Fuck******]]]##########################
@app.route("/candidatos/<string:id>/partidos/<string:id_p>",methods=['PUT'])
def asignarPartidoCandidato(id, id_p):
    json = miControladorCandidatos.asignarPartido(id, id_p)
    return jsonify(json)

##########################[[[Partidos]]]##########################
@app.route("/partidos", methods=['GET'])
def getPartidos():
    json = miControladorPartidos.index()
    return jsonify(json)

@app.route("/partidos", methods=['POST'])
def crearPartido():
    data = request.get_json()
    json = miControladorPartidos.create(data)
    return jsonify(json)

@app.route("/partidos/<string:id>", methods=['GET'])
def getPartido(id):
    json = miControladorPartidos.show(id)
    return jsonify(json)

@app.route("/partidos/<string:id>", methods=['PUT'])
def modificarPartido(id):
    data = request.get_json()
    json = miControladorPartidos.update(id, data)
    return jsonify(json)

@app.route("/partidos/<string:id>", methods=['DELETE'])
def eliminarPartido(id):
    json = miControladorPartidos.delete(id)
    return jsonify(json)

##########################[[[Mesas]]]##########################
@app.route("/mesas", methods=['GET'])
def getMesas():
    json = miControladorMesas.index()
    return jsonify(json)

@app.route("/mesas", methods=['POST'])
def crearMesa():
    data = request.get_json()
    json = miControladorMesas.create(data)
    return jsonify(json)

@app.route("/mesas/<string:id>", methods=['GET'])
def getMesa(id):
    json = miControladorMesas.show(id)
    return jsonify(json)

@app.route("/mesas/<string:id>", methods=['PUT'])
def modificarMesa(id):
    data = request.get_json()
    json = miControladorMesas.update(id, data)
    return jsonify(json)

@app.route("/mesas/<string:id>", methods=['DELETE'])
def eliminarMesa(id):
    json = miControladorMesas.delete(id)
    return jsonify(json)

##########################[[[Resultados]]]##########################
@app.route("/resultados", methods=['GET'])
def getResultados():
    json = miControladorResultados.index()
    return jsonify(json)

@app.route("/resultados", methods=['POST'])
def crearResultado():
    data = request.get_json()
    json = miControladorResultados.create(data)
    return jsonify(json)

@app.route("/resultados/<string:id>", methods=['GET'])
def getResultado(id):
    json = miControladorResultados.show(id)
    return jsonify(json)

@app.route("/resultados/<string:id>", methods=['PUT'])
def modificarReultado(id):
    data = request.get_json()
    json = miControladorResultados.update(id, data)
    return jsonify(json)

@app.route("/resultados/<string:id>", methods=['DELETE'])
def eliminarResultado(id):
    json = miControladorResultados.delete(id)
    return jsonify(json)

####################################################################################
def loadFileConfig():
    with open('config.json') as f:
        data = json.load(f)
    return data

if __name__ == '__main__':
    dataConfig = loadFileConfig()
    print("Server running : " + "http://" + dataConfig["url-backend"] + ":" + str(dataConfig["port"]))
    serve(app, host=dataConfig["url-backend"], port=dataConfig["port"])
####################################################################################