from Repositorios.PartidosRepositorio import PartidosRepositorio
from Modelos.Partidos import Partidos

class ControladorPartidos():
    def __init__(self):
        self.repositorioPartidos = PartidosRepositorio()

    def index(self):
        return self.repositorioPartidos.findAll()

    def create(self,infoPartido):
        nuevoPartido = Partidos(infoPartido)
        return self.repositorioPartidos.save(nuevoPartido)

    def show(self, id):
        elPartido = Partidos(self.repositorioPartidos.findById(id))
        return elPartido.__dict__

    def update(self,id,infoPartido):
        actualPartido = Partidos(self.repositorioPartidos.findById(id))
        actualPartido.nombre_partido = infoPartido['nombre_partido']
        actualPartido.lema = infoPartido['lema']
        return self.repositorioPartidos.save(actualPartido)

    def delete(self,id):
       return self.repositorioPartidos.delete(id)

