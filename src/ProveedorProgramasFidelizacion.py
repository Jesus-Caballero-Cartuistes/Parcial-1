from src.Proveedor import Proveedor


class ProveedorProgramasFidelizacion(Proveedor):
    def __init__(self, nombre):
        super().__init__(nombre)
        self.tipo_programa = "programa_fidelizacion"
