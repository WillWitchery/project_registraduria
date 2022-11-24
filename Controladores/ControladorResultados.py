from Repositorios.ResultadosRepositorio import ResultadosRepositorio
from Repositorios.MesasRepositorio import MesasRepositorio
from Modelos.Resultados import Resultados
from Modelos.Mesas import Mesas

class ControladorResultados():
    def __init__(self):
        self.repositorioResultados = ResultadosRepositorio()
        self.repositorioMesas = MesasRepositorio()

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
    
    def asignarMesa(self,id,id_m):
        resultadoActual = Resultados(self.repositorioResultados.findById(id))
        mesaActual = Mesas(self.repositorioMesas.findById(id_m))
        resultadoActual.mesa = mesaActual
        return self.repositorioResultados.save(resultadoActual)
    
