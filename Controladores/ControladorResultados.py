from Repositorios.ResultadosRepositorio import ResultadosRepositorio
from Modelos.Resultados import Resultados

class ControladorResultados():
    def __init__(self):
        self.repositorioResultados = ResultadosRepositorio()

    def index(self):
        return self.repositorioResultados.findAll()

    def create(self,infoResultados):
        nuevoResultado = Resultados(infoResultados)
        return self.repositorioResultados.save(nuevoResultado)

    def show(self, id):
        elResultado = Resultados(self.repositorioResultados.findById(id))
        return elResultado.__dict__

    def update(self,id,infoResultado):
        actualResultado = Resultados(self.repositorioResultados.findById(id))
        actualResultado.numero_mesa = infoResultado['numero_mesa']
        actualResultado.registro_votos = infoResultado['registro_votos']
        return self.repositorioResultados.save(actualResultado)

    def delete(self,id):
       return self.repositorioResultados.delete(id)