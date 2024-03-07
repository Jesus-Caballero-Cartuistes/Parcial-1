from abc import ABC, abstractmethod


class Proveedor(ABC):
    def __init__(self, nombre):
        self.nombre = nombre

    @abstractmethod
    def obtener_productos(self):
        pass
