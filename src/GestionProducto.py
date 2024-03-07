from src.interfaces.Gestion import Gestion
from src.microservices.ProductoMicroservicio import ProductoMicroservicio
from Producto import Producto


class GestionProducto(Gestion):
    def __init__(self):
        self.microservicio_productos = ProductoMicroservicio()
        self.producto = Producto(None, None, None,None)

    def agregar(self, producto):
        # Agregar un nuevo producto al microservicio
        tipo = producto.categoria
        self.microservicio_productos.productos[tipo].append({
            "nombre": producto.nombre,
            "descripcion": producto.descripcion,
            "proveedor": producto.proveedor,
            "precio": producto.precio,
            "categorias": producto.categoria
        })

    def eliminar(self, clave):
        # Eliminar un producto basado en su nombre (clave)
        for tipo, productos in self.microservicio_productos.productos.items():
            self.microservicio_productos.productos[tipo] = [producto for producto in productos if producto["nombre"] != clave]

    def obtener(self, clave):
        # Obtener un producto por su nombre (clave)
        for tipo, productos in self.microservicio_productos.productos.items():
            for producto in productos:
                if producto["nombre"] == clave:
                    return producto
        return None

    def listar(self):
        # Listar todos los productos
        todos_los_productos = []
        for productos in self.microservicio_productos.productos.values():
            todos_los_productos.extend(productos)
        return todos_los_productos
