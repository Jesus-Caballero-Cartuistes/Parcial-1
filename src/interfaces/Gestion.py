from abc import ABC, abstractmethod


class Gestion(ABC):
    @abstractmethod
    def agregar(self, item):
        pass

    @abstractmethod
    def eliminar(self, clave):
        pass

    @abstractmethod
    def obtener(self, clave):
        pass

    @abstractmethod
    def listar(self):
        pass
