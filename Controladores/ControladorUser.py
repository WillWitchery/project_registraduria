from Repositorios.UserRepositorio import UserRepositorio
from Modelos.User import User

class ControladorUser():
    def __init__(self):
        self.repositorioUser = UserRepositorio()

    def index(self):
        return self.repositorioUser.findAll()

    def create(self,infoUser):
        nuevoUser = User(infoUser)
        return self.repositorioUser.save(nuevoUser)

    def show(self, id):
        elUser = User(self.repositorioUser.findById(id))
        return elUser.__dict__

    def update(self,id,infoUser):
        actualUser = User(self.repositorioUser.findById(id))
        actualUser.usuario = infoUser['usuario']
        actualUser.correo = infoUser['correo']
        actualUser.contrasena = infoUser['contrasena']
        return self.repositorioUser.save(actualUser)

    def delete(self,id):
       return self.repositorioUser.delete(id)