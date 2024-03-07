from src.Usuario import Usuario
from src.microservices.ClientesMicroservicio import ClientesMicroservicio
from src.interfaces.Autenticacion import Autenticacion


class AutenticacionUsuario(Autenticacion):
    def __init__(self):
        self.clientesMicroservicio = ClientesMicroservicio()

    def iniciar_sesion(self, usuario: Usuario):
        return self.clientesMicroservicio.verificar_credenciales(usuario)

    def cerrar_sesion(self, nombre_usuario):
        # Lógica para cerrar la sesión del usuario (si es necesario)
        pass
