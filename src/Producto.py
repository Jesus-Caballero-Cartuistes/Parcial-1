from Proveedor import Proveedor


class Producto:
    def __init__(self, nombre, precio, descripcion, proveedor: Proveedor):
        self.nombre = nombre
        self.precio = precio
        self.descripcion = descripcion
        self.categoria = []
        self.proveedor = proveedor

    def asignar_proveedor(self, proveedor):
        self.proveedor = proveedor

    def mostrar_informacion(self):
        return f"Nombre: {self.nombre}, Precio: {self.precio}, Descripción: {self.descripcion}"
