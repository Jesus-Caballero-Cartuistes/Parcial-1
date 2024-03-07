# Importamos los microservicios from usuario_Microservice import UsuarioService
from AutenticacionUsuario import AutenticacionUsuario
from Usuario import Usuario
from src.Cliente import Cliente
from GestionProducto import GestionProducto
from GestionUsuario import GestionUsuario
from RecomendacionProducto import RecomendacionProducto


class Main:
    autenticacionUsuario = AutenticacionUsuario()
    gestionUsuario = GestionUsuario()
    gestionProducto = GestionProducto()
    recomendacionProducto = RecomendacionProducto()

    # Función para mostrar el menú principal
    def mostrar_menu_principal(self):
        while True:
            print()
            print("Bienvenido a nuestra plataforma de servicios financieros. Por favor, seleccione una opción:")
            print("1. Iniciar sesión")
            print("2. Registrarse")
            print("3. Salir")

            opcion = input("Ingrese el número de la opción que desea: ")

            if opcion == "1":
                # Lógica para iniciar sesión utilizando el servicio de autenticación
                correo = input("Ingrese su correo: ")
                contrasena = input("Ingrese su contraseña: ")
                usuario = Usuario(None, correo, contrasena)
                self.iniciar_sesion(usuario)
            elif opcion == "2":
                # Lógica para registrar un nuevo usuario utilizando el servicio de usuarios
                nombre = input("Ingrese su nombre: ")
                correo = input("Ingrese un correo: ")
                contrasena = input("Ingrese una contraseña: ")
                usuario = Cliente(nombre, correo, contrasena, None)
                self.registrarse(usuario)
            elif opcion == "3":
                print("Gracias por usar nuestra plataforma. ¡Hasta luego!")
                break
            else:
                print("Opción no válida. Por favor, seleccione una opción válida.")

    # Función para mostrar el menú secundario
    def mostrar_menu_secundario(self, usuario: Usuario):
        while True:
            print()
            print("Seleccione una opción:")
            print("1. Ver productos disponibles")
            print("2. ¡Recomendaciones!")
            print("3. Cerrar sesión")

            opcion = input("Ingrese el número de la opción que desea: ")

            if opcion == "1":
                productos = self.gestionProducto.listar()
                self.imprimir_productos(productos)

            elif opcion == "2":
                recomendaciones = self.recomendacionProducto.obtener_recomendaciones_para_usuario(usuario.correo)
                if not recomendaciones:
                    print("No hay suficientes datos para recomendar productos.")
                self.imprimir_productos(recomendaciones)

            elif opcion == "3":
                print("Cerrando sesión. ¡Hasta luego!")
                break
            else:
                print("Opción no válida. Por favor, seleccione una opción válida.")

    # Función para iniciar sesión
    def iniciar_sesion(self, usuario: Usuario):
        if self.autenticacionUsuario.iniciar_sesion(usuario):
            print("Inicio de sesión exitoso. ¡Bienvenido de nuevo!")
            self.mostrar_menu_secundario(usuario)
        else:
            print("Nombre de usuario o contraseña incorrectos. Por favor, inténtelo nuevamente.")

    # Función para registrar un nuevo usuario
    def registrarse(self, usuario: Cliente):
        if self.gestionUsuario.agregar(usuario):
            print("¡Registro exitoso! Ahora puede iniciar sesión.")
        else:
            print("Hubo un problema al registrar el usuario. Por favor, inténtelo nuevamente.")

    def imprimir_productos(self, productos):
        if not productos:
            print("No hay productos disponibles.")
        else:
            for producto in productos:
                print("Nombre:", producto["nombre"])
                print("Descripción:", producto["descripcion"])
                print("Proveedor:", producto["proveedor"])
                print("Precio:", producto["precio"])
                print()  # Espacio en blanco entre productos


# Crear una instancia de la clase Main
main = Main()
# Llamar al método mostrar_menu_principal de la instancia main
main.mostrar_menu_principal()
