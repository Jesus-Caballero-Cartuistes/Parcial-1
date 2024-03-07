from src.interfaces.Gestion import Gestion
from src.microservices.ClientesMicroservicio import ClientesMicroservicio
from Usuario import Usuario


class GestionUsuario(Gestion):
    def __init__(self):
        self.microservicio_usuarios = ClientesMicroservicio()
        self.usuario = Usuario(None, None, None)

    def agregar(self, usuario):
        # Supongamos que 'usuario' es una instancia de la clase Usuario
        correo = usuario.correo
        if correo:
            return self.microservicio_usuarios.agregar_cliente(usuario)
        else:
            raise ValueError("Falta el correo del usuario")

    def obtener(self, clave):
        # 'clave' es el correo electrónico del usuario
        return self.microservicio_usuarios.obtener_cliente(clave)

    def eliminar(self, clave):
        # Aquí, 'clave' es el correo del usuario
        return self.microservicio_usuarios.eliminar_usuario(clave)

    def listar(self):
        pass  # No implementamos la función listar en esta clase