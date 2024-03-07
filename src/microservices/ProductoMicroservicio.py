class ProductoMicroservicio:
    def __init__(self):
        # Base de datos de ejemplo de productos (solo para propósitos de demostración)
        self.productos = {
            "seguro_auto": [
                {
                    "nombre": "Seguro de Auto Básico",
                    "descripcion": "Protege tu automóvil contra daños y robos",
                    "proveedor": "Compañía de Seguros ABC",
                    "precio": 100.00,
                    "categorias": ["seguridad vehicular", "cobertura básica"]
                },
                {
                    "nombre": "Seguro de Auto Premium",
                    "descripcion": "Ofrece una cobertura amplia y servicios adicionales",
                    "proveedor": "Compañía de Seguros XYZ",
                    "precio": 200.00,
                    "categorias": ["seguridad vehicular", "beneficios premium"]
                }
            ],
            "tarjeta_credito": [
                {
                    "nombre": "Tarjeta de Crédito Básica",
                    "descripcion": "Tarjeta de crédito con tasas competitivas",
                    "proveedor": "Banco XYZ",
                    "precio": 0.00,
                    "categorias": ["finanzas", "crédito básico"]  # Categoría añadida
                },
                {
                    "nombre": "Tarjeta de Crédito Premium",
                    "descripcion": "Tarjeta con beneficios exclusivos y tasas preferenciales",
                    "proveedor": "Banco ABC",
                    "precio": 0.00,
                    "categorias": ["finanzas", "beneficios premium"]  # Categoría añadida
                }
            ],
            "programa_fidelizacion": [
                {
                    "nombre": "Programa de Fidelización Estándar",
                    "descripcion": "Obtén recompensas por tus compras y acumula puntos",
                    "proveedor": "Tienda de Departamentos ABC",
                    "precio": 0.00,
                    "categorias": ["compras", "fidelización estándar"]  # Categoría añadida
                },
                {
                    "nombre": "Programa de Fidelización VIP",
                    "descripcion": "Accede a beneficios exclusivos y promociones especiales",
                    "proveedor": "Tienda de Departamentos XYZ",
                    "precio": 0.00,
                    "categorias": ["compras", "fidelización VIP"]  # Categoría añadida
                }
            ]
        }

    def obtener_productos_por_tipo(self, tipo):
        if tipo in self.productos:
            return self.productos[tipo]
        else:
            return []

    def obtener_productos_por_categoria(self, categoria):
        productos_por_categoria = []
        for tipo, productos in self.productos.items():
            for producto in productos:
                if categoria in producto.get("categorias", []):
                    productos_por_categoria.append(producto)
        return productos_por_categoria