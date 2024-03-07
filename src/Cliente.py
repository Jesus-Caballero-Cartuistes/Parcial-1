from src.Usuario import Usuario


class Cliente(Usuario):
    def __init__(self, nombre, correo, contrasena, preferencias):
        super().__init__(nombre, correo, contrasena)
        if preferencias is None:
            preferencias = []
        self.preferencias = preferencias

    def agregar_preferencia(self, preferencia):
        self.preferencias.append(preferencia)

    def eliminar_preferencia(self, preferencia):
        if preferencia in self.preferencias:
            self.preferencias.remove(preferencia)
