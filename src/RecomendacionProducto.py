from src.microservices.RecomendacionMicroservicio import RecomendacionMicroservicio
from GestionUsuario import GestionUsuario


class RecomendacionProducto:
    def __init__(self):
        self.gestion_usuario = GestionUsuario()
        self.recomendacion_microservicio = RecomendacionMicroservicio()

    def obtener_recomendaciones_para_usuario(self, correo_usuario):
        # Obtener datos del usuario, incluidas sus categorías de interés
        usuario = self.gestion_usuario.obtener(correo_usuario)
        if not usuario:
            return "Usuario no encontrado."
        categorias_interes = usuario.preferencias
        if not categorias_interes:
            return "No hay categorías de interés registradas para este usuario."

        # Obtener recomendaciones de productos basadas en las categorías de interés del usuario
        recomendaciones = self.recomendacion_microservicio.recomendar_productos_por_categorias(categorias_interes)

        return recomendaciones
