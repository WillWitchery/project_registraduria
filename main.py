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
from Controladores.ControladorCandidatos import ControladorCandidatos
from Controladores.ControladorPartidos import ControladorPartidos
from Controladores.ControladorMesas import ControladorMesas
from Controladores.ControladorResultados import ControladorResultados
from Controladores.ControladorInscripciones import ControladorInscripciones
miControladorCandidatos = ControladorCandidatos()
miControladorPartidos = ControladorPartidos()
miControladorMesas = ControladorMesas()
miControladorResultados = ControladorResultados()
miControladorInscripcion = ControladorInscripciones()

##########################[[[Server]]]#####################################
@app.route("/", methods=['GET'])
def test():
    json = {}
    json["message"] = "Server running ..."
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

##########################[[[******Asignaciones******]]]##########################
@app.route("/candidatos/<string:id>/partidos/<string:id_p>",methods=['PUT'])
def asignarPartidoaCandidato(id, id_p):
    json = miControladorCandidatos.asignarPartido(id, id_p)
    return jsonify(json)

@app.route("/mesas/<string:id>/candidatos/<string:id_c>",methods=['PUT'])
def asignarCandidatoaMesa(id, id_c):
    json = miControladorMesas.asignarCandidato(id, id_c)
    return jsonify(json)

@app.route("/resultados/<string:id>/mesas/<string:id_m>",methods=['PUT'])
def asignarMesaaResultado(id, id_m):
    json = miControladorResultados.asignarMesa(id, id_m)
    return jsonify(json)

##########################[[[******Inscripciones******]]]##########################
@app.route("/inscripciones",methods=['GET'])
def getInscripciones():
    json=miControladorInscripcion.index()
    return jsonify(json)

@app.route("/inscripciones/<string:id>",methods=['GET'])
def getInscripcion(id):
    json=miControladorInscripcion.show(id)
    return jsonify(json)

@app.route("/inscripciones/partidos/<string:id_p>/candidatos/<string:id_c>/mesas/<string:id_m>/resultados/<string:id_r>",methods=['POST'])
def crearInscripcion(id_p, id_c, id_m, id_r):
    data = request.get_json()
    json=miControladorInscripcion.create(data, id_p, id_c, id_m, id_r)
    return jsonify(json)

@app.route("/inscripciones/<string:id_ins>/partidos/<string:id_p>/candidatos/<string:id_c>/mesas/<string:id_m>/resultados/<string:id_r>",methods=['PUT'])
def modificarInscripcion(id_ins, id_p, id_c, id_m, id_r):
    data = request.get_json()
    json=miControladorInscripcion.update(id_ins, id_p, id_c, id_m, id_r)
    return jsonify(json)

@app.route("/inscripciones/<string:id_inscripcion>",methods=['DELETE'])
def eliminarInscripcion(id_inscripcion):
    json=miControladorInscripcion.delete(id_inscripcion)
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