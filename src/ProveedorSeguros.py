from src.Proveedor import Proveedor


class ProveedorSeguros(Proveedor):
    def __init__(self, nombre):
        super().__init__(nombre)
        self.tipo_seguro = "seguro_auto"
