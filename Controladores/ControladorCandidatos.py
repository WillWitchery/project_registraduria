from Repositorios.CandidatosRepositorio import CandidatosRepositorio
from Repositorios.PartidosRepositorio import PartidosRepositorio
from Modelos.Candidatos import Candidatos
from Modelos.Partidos import Partidos

class ControladorCandidatos():
    def __init__(self):
        self.repositorioCandidatos = CandidatosRepositorio()
        self.repositorioPartidos = PartidosRepositorio()

    def index(self):
        return self.repositorioCandidatos.findAll()

    def create(self,infoCandidato):
        nuevoCandidato = Candidatos(infoCandidato)
        return self.repositorioCandidatos.save(nuevoCandidato)

    def show(self, id):
        elCandidato = Candidatos(self.repositorioCandidatos.findById(id))
        return elCandidato.__dict__

    def update(self,id,infoCandidato):
        actualCandidato = Candidatos(self.repositorioCandidatos.findById(id))
        actualCandidato.resolucion_acreditacion = infoCandidato['resolucion_acreditacion']
        actualCandidato.cedula = infoCandidato['cedula']
        actualCandidato.nombre = infoCandidato['nombre']
        actualCandidato.apellido = infoCandidato['apellido']
        return self.repositorioCandidatos.save(actualCandidato)

    def delete(self,id):
       return self.repositorioCandidatos.delete(id)

    def asignarPartido(self, id, id_p):
        actualCandidato = Candidatos(self.repositorioCandidatos.findById(id))
        actualPartido = Partidos(self.repositorioPartidos.findById(id_p))
        actualCandidato.partido = actualPartido
        return self.repositorioCandidatos.save(actualCandidato)