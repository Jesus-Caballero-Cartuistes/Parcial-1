from src.Usuario import Usuario
from src.Cliente import Cliente


class ClientesMicroservicio:
    def __init__(self):
        # Base de datos ficticia de usuarios (solo para propósitos de demostración)
        self.usuarios = {
            'usuario1@example.com': {'contrasena': 'contraseña1', 'nombre': 'Usuario1',
                                     'preferencias': ["finanzas", "beneficios premium"]},
            'usuario2@example.com': {'contrasena': 'contraseña2', 'nombre': 'Usuario2',
                                     'preferencias': ["noticias", "viajes"]}
        }

    def verificar_credenciales(self, usuario):
        correo = usuario.correo
        contrasena = usuario.contrasena
        if correo in self.usuarios and self.usuarios[correo]['contrasena'] == contrasena:
            return self.usuarios[correo]  # Retorna los datos del usuario autenticado
        else:
            return None  # Retorna None si las credenciales son inválidas

    def agregar_cliente(self, cliente):
        # Agrega un nuevo cliente a la base de datos
        correo = cliente.correo
        if correo not in self.usuarios:
            self.usuarios[correo] = {
                'contrasena': cliente.contrasena,
                'nombre': cliente.nombre,
                'preferencias': cliente.preferencias
            }
            return True
        else:
            return False  # El usuario ya existe

    def obtener_cliente(self, correo):
        # Obtiene un objeto de usuario a partir de su correo
        if correo in self.usuarios:
            usuario_info = self.usuarios[correo]
            return Cliente(correo, usuario_info['contrasena'], usuario_info['nombre'], usuario_info['preferencias'])
        else:
            return None  # Retorna None si no se encuentra el usuario

    def eliminar_usuario(self, correo):
        # Elimina un usuario de la base de datos a partir de su correo
        if correo in self.usuarios:
            del self.usuarios[correo]
            return True  # Retorna True si el usuario fue eliminado exitosamente
        else:
            return False  # Retorna False si el usuario no existe