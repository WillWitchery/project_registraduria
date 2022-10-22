from Modelos.User import User

class ControladorUser():
    def __init__(self):
        print("Creando ControladorUsuario")

    def index(self):
        print("Listar todos los usuarios")
        unUsuario = {
            "usuario": "abc123",
            "correo": "juan@gmail.com",
            "contraseña": "Juan",
         }
        return [unUsuario]

    def create(self,infoUser):
        print("Crear un usuario")
        elUsuario = User(infoUser)
        return elUsuario.__dict__

    def show(self,id):
        print("Mostrando un usuario con id ",id)
        elUsuario = {
            "usuario": "abc123",
            "correo": "juan@gmail.com",
            "contraseña": "Juan",
        }
        return elUsuario

    def update(self,id,infoEstudiante):
        print("Actualizando usuario con id ",id)
        print("Actualizando usuario con id ", id)
        elUsuario = User(infoEstudiante)
        return elUsuario.__dict__

    def delete(self,id):
        print("Elimiando usuario con id ",id)
        return {"deleted_count": 1}