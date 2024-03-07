from src.Proveedor import Proveedor


class ProveedorTarjetasCredito(Proveedor):
    def __init__(self, nombre):
        super().__init__(nombre)
        self.tipo_tarjeta = "tarjeta_credito"
