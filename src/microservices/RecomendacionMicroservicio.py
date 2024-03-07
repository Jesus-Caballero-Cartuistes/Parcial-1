from src.microservices.ProductoMicroservicio import ProductoMicroservicio


class RecomendacionMicroservicio:
    def __init__(self):
        self.producto_microservicio = ProductoMicroservicio()

    def recomendar_productos_por_categorias(self, preferencias):
        recomendaciones = []
        for preferencia in preferencias:
            productos = self.producto_microservicio.obtener_productos_por_categoria(preferencia)
            for producto in productos:
                if producto not in recomendaciones:  # Evitar duplicados
                    recomendaciones.append(producto)
        return recomendaciones
