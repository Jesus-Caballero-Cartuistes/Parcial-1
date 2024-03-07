
import unittest
from unittest.mock import MagicMock

from src.AutenticacionUsuario import AutenticacionUsuario
from src.GestionUsuario import GestionUsuario
from src.RecomendacionProducto import RecomendacionProducto
from src.Usuario import Usuario


class Test(unittest.TestCase):
    def setUp(self):
        self.autenticacion = AutenticacionUsuario()
        self.gestion_usuario = GestionUsuario()
        self.recomendacion_producto = RecomendacionProducto()

        # Mock del microservicio de usuarios para simular su comportamiento
        self.gestion_usuario.microservicio_usuarios = MagicMock()

        # Mock del gestor de usuarios para simular su comportamiento
        self.recomendacion_producto.gestion_usuario = MagicMock()

        # Mock del microservicio de recomendaciones para simular su comportamiento
        self.recomendacion_producto.recomendacion_microservicio = MagicMock()

    def test_iniciar_sesion_usuario_valido(self):
        # Crear un usuario válido
        usuario_valido = Usuario(None, 'usuario1@example.com', 'contraseña1')

        # Intentar iniciar sesión con el usuario válido
        resultado = self.autenticacion.iniciar_sesion(usuario_valido)

        # Verificar que el resultado sea verdadero (indicando inicio de sesión exitoso)
        self.assertTrue(resultado)

    def test_iniciar_sesion_usuario_invalido(self):
        # Crear un usuario con credenciales inválidas
        usuario_invalido = Usuario(None, 'usuario3@example.com', 'contraseña3')

        # Intentar iniciar sesión con el usuario inválido
        resultado = self.autenticacion.iniciar_sesion(usuario_invalido)

        # Verificar que el resultado sea falso (indicando inicio de sesión fallido)
        self.assertFalse(resultado)

    def test_agregar_usuario_exitoso(self):
        # Creamos un usuario válido
        usuario = Usuario("John Doe", "john@example.com", "password")

        # Configuramos el comportamiento del mock para agregar correctamente el usuario
        self.gestion_usuario.microservicio_usuarios.agregar_cliente.return_value = True

        # Intentamos agregar el usuario
        resultado = self.gestion_usuario.agregar(usuario)

        # Verificamos que la función devuelva True (indicando que el usuario se agregó correctamente)
        self.assertTrue(resultado)

    def test_agregar_usuario_falta_correo(self):
        # Creamos un usuario sin correo
        usuario = Usuario("John Doe", None, "password")

        # Intentamos agregar el usuario sin correo (debería generar una excepción)
        with self.assertRaises(ValueError):
            self.gestion_usuario.agregar(usuario)

    def test_obtener_usuario_existente(self):
        # Configuramos el comportamiento del mock para obtener un usuario existente
        self.gestion_usuario.microservicio_usuarios.obtener_cliente.return_value = Usuario("John Doe", "john@example.com", "password")

        # Intentamos obtener un usuario existente
        usuario_obtenido = self.gestion_usuario.obtener("john@example.com")

        # Verificamos que el usuario obtenido no sea None
        self.assertIsNotNone(usuario_obtenido)

    def test_obtener_usuario_no_existente(self):
        # Configuramos el comportamiento del mock para obtener un usuario no existente
        self.gestion_usuario.microservicio_usuarios.obtener_cliente.return_value = None

        # Intentamos obtener un usuario no existente
        usuario_obtenido = self.gestion_usuario.obtener("nonexistent@example.com")

        # Verificamos que el usuario obtenido sea None
        self.assertIsNone(usuario_obtenido)

    def test_eliminar_usuario_exitoso(self):
        # Configuramos el comportamiento del mock para eliminar un usuario existente
        self.gestion_usuario.microservicio_usuarios.eliminar_usuario.return_value = True

        # Intentamos eliminar un usuario existente
        resultado = self.gestion_usuario.eliminar("usuario1@example.com")

        # Verificamos que la función devuelva True (indicando que el usuario se eliminó correctamente)
        self.assertTrue(resultado)

    def test_eliminar_usuario_no_existente(self):
        # Configuramos el comportamiento del mock para eliminar un usuario no existente
        self.gestion_usuario.microservicio_usuarios.eliminar_usuario.return_value = False

        # Intentamos eliminar un usuario no existente
        resultado = self.gestion_usuario.eliminar("nonexistent@example.com")

        # Verificamos que la función devuelva False (indicando que el usuario no se pudo eliminar)
        self.assertFalse(resultado)

    def test_obtener_recomendaciones_para_usuario_existente(self):
        # Configuramos el comportamiento del mock para obtener un usuario existente con preferencias
        usuario_existente = MagicMock()
        usuario_existente.preferencias = ["finanzas", "viajes"]
        self.recomendacion_producto.gestion_usuario.obtener.return_value = usuario_existente

        # Configuramos el comportamiento del mock para devolver recomendaciones
        recomendaciones_esperadas = ["Producto1", "Producto2", "Producto3"]
        self.recomendacion_producto.recomendacion_microservicio.recomendar_productos_por_categorias.return_value = recomendaciones_esperadas

        # Intentamos obtener recomendaciones para un usuario existente
        recomendaciones_obtenidas = self.recomendacion_producto.obtener_recomendaciones_para_usuario("usuario@example.com")

        # Verificamos que las recomendaciones obtenidas coincidan con las esperadas
        self.assertEqual(recomendaciones_obtenidas, recomendaciones_esperadas)

    def test_obtener_recomendaciones_para_usuario_no_existente(self):
        # Configuramos el comportamiento del mock para obtener un usuario no existente
        self.recomendacion_producto.gestion_usuario.obtener.return_value = None

        # Intentamos obtener recomendaciones para un usuario no existente
        resultado = self.recomendacion_producto.obtener_recomendaciones_para_usuario("nonexistent@example.com")

        # Verificamos que el resultado sea una cadena indicando que el usuario no fue encontrado
        self.assertEqual(resultado, "Usuario no encontrado.")

    def test_obtener_recomendaciones_para_usuario_sin_preferencias(self):
        # Configuramos el comportamiento del mock para obtener un usuario existente sin preferencias
        usuario_existente = MagicMock()
        usuario_existente.preferencias = []
        self.recomendacion_producto.gestion_usuario.obtener.return_value = usuario_existente

        # Intentamos obtener recomendaciones para un usuario existente sin preferencias
        resultado = self.recomendacion_producto.obtener_recomendaciones_para_usuario("usuario@example.com")

        # Verificamos que el resultado sea una cadena indicando que no hay preferencias registradas
        self.assertEqual(resultado, "No hay categorías de interés registradas para este usuario.")


if __name__ == '__main__':
    unittest.main()
