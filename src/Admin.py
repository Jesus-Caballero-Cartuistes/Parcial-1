from src.Usuario import Usuario


class Admin(Usuario):
    def __init__(self, nombre, correo, contrasena, rol):
        super().__init__(nombre, correo, contrasena)
        self.rol = rol
