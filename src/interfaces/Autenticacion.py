from abc import ABC, abstractmethod
from src.Usuario import Usuario


class Autenticacion(ABC):
    @abstractmethod
    def iniciar_sesion(self, usuario: Usuario):
        pass

