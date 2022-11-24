from Modelos.Inscripciones import Inscripciones
from Modelos.Candidatos import Candidatos
from Modelos.Mesas import Mesas
from Modelos.Partidos import Partidos
from Modelos.Resultados import Resultados
from Repositorios.InscripcionesRepositorio import InscripcionesRepositorio
from Repositorios.CandidatosRepositorio import CandidatosRepositorio
from Repositorios.MesasRepositorio import MesasRepositorio
from Repositorios.PartidosRepositorio import PartidosRepositorio
from Repositorios.ResultadosRepositorio import ResultadosRepositorio

class ControladorInscripciones():
    def __int__(self):
        self.repositorioInscripcion = InscripcionesRepositorio()
        self.repositorioCandidato = CandidatosRepositorio()
        self.repositorioMesa = MesasRepositorio()
        self.repositorioPartido = PartidosRepositorio()
        self.repositorioResultado = ResultadosRepositorio()

    def __index__(self):
        return self.repositorioInscripcion.findAll()

    def create (self, info_ins, id_p, id_c, id_m, id_r):
        nuevaInscripcion = Inscripciones (info_ins)
        _partido = Partidos (self.repositorioPartido.findById(id_p))
        _candidato = Candidatos (self.repositorioCandidato.findById(id_c))
        _mesa = Mesas (self.repositorioMesa.findById(id_m))
        _resultado = Resultados (self.repositorioResultado.findById(id_r))
        nuevaInscripcion.partido = _partido
        nuevaInscripcion.candidato = _candidato
        nuevaInscripcion.mesa = _mesa
        nuevaInscripcion.resultado = _resultado
        return self.repositorioInscripcion.save(nuevaInscripcion)

    def show (self, id):
        dataInscripcion = Inscripciones (self.repositorioInscripcion.findById(id))
        return dataInscripcion.__dict__

    def update (self, id_ins, info_ins, id_p, id_c, id_m, id_r):
        infoInscripcion = Inscripciones (self.repositorioInscripcion.findById(id_ins))
        infoInscripcion.fecha =  info_ins("fecha")
        infoInscripcion.comentario = info_ins("comentario")
        _partido = Partidos(self.repositorioPartido.findById(id_p))
        _candidato = Candidatos(self.repositorioCandidato.findById(id_c))
        _mesa = Mesas(self.repositorioMesa.findById(id_m))
        _resultado = Resultados(self.repositorioResultado.findById(id_r))
        infoInscripcion.partido = _partido
        infoInscripcion.candidato = _candidato
        infoInscripcion.mesa = _mesa
        infoInscripcion.resultadp = _resultado
        return self.repositorioInscripcion.save(infoInscripcion)

    def delete (self, id):
        return self.repositorioInscripcion.delete(id)




