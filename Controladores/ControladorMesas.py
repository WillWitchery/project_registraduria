from Repositorios.MesasRepositorio import MesasRepositorio
from Modelos.Mesas import Mesas

class ControladorMesas():
    def __init__(self):
        self.repositorioMesas = MesasRepositorio()

    def index(self):
        return self.repositorioMesas.findAll()

    def create(self,infoMesas):
        nuevaMesa = Mesas(infoMesas)
        return self.repositorioMesas.save(nuevaMesa)

    def show(self, id):
        laMesa = Mesas(self.repositorioMesas.findById(id))
        return laMesa.__dict__

    def update(self,id,infoMesa):
        actualMesa = Mesas(self.repositorioMesas.findById(id))
        actualMesa.numero_mesa = infoMesa['numero_mesa']
        actualMesa.cedulas_inscritas = infoMesa['cedulas_inscritas']
        actualMesa.candidatos_votar = infoMesa['candidatos_votar']
        return self.repositorioMesas.save(actualMesa)


    def delete(self,id):
       return self.repositorioMesas.delete(id)