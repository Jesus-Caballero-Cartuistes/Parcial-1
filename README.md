## Sistema de Recomendación de Productos

------------
En una era donde la tecnología redefine constantemente las expectativas de los consumidores, una empresa emergente visionaria se embarcó en una misión para revolucionar la forma en que las personas interactúan con y aprovechan sus múltiples beneficios financieros y de servicios. Inspirados por la complejidad que enfrentaban los usuarios al gestionar sus beneficios dispersos en seguros, tarjetas de crédito, y programas de fidelización, el equipo se propuso construir un sistema unificado que no solo centralizara estos beneficios en una sola plataforma, sino que también orientara a los usuarios hacia la maximización de su valor en cada compra. Este sistema integrado de beneficios se convirtió en la piedra angular de su visión, prometiendo una interfaz intuitiva respaldada por una arquitectura robusta y un motor de recomendaciones inteligente.

Al abordar el diseño del sistema, la elección de una arquitectura de microservicios emergió como la solución óptima, promoviendo la flexibilidad, la escalabilidad y la facilidad de integración con sistemas externos. Esta arquitectura facilitaría la actualización y expansión continuas del sistema, permitiendo al equipo añadir nuevos proveedores de beneficios o actualizar los existentes sin interrupciones significativas.

Por otra parte, la identificación de los requerimientos críticos, equilibrando cuidadosamente las necesidades funcionales, como la integración transparente con diversos proveedores de beneficios y un sistema de recomendaciones altamente personalizado, con imperativos no funcionales como seguridad de datos, escalabilidad y disponibilidad. La meta es crear un sistema que no solo respondiera a las necesidades actuales de los usuarios, sino que también pudiera adaptarse a las demandas futuras.

La presentación clara de los beneficios disponibles, junto con una retroalimentación inmediata y relevante sobre las recomendaciones de beneficios, se convirtió en una prioridad para asegurar que los usuarios pudieran tomar decisiones informadas con facilidad. Así mismo, con los cimientos tecnológicos en su lugar, la experiencia del usuario debe ser visualmente atractiva y accesible en una variedad de dispositivos, si no que también proporcionara una interacción intuitiva con el sistema.

La implementación del sistema debe seguir los principios SOLID para asegurar un código mantenible y extensible. Cada microservicio debe ser construido con un propósito específico, desde gestionar la autenticación de usuarios hasta procesar complejas recomendaciones de beneficios. La seguridad fue debe estar en cada etapa empleando las mejores prácticas para proteger la información personal y financiera de los usuarios.

## Diagrama de Clases
[![diagrama de clases](https://github.com/Jesus-Caballero-Cartuistes/Parcial-1/blob/master/classes.png "diagrama de clases")](https://github.com/Jesus-Caballero-Cartuistes/Parcial-1/blob/master/classes.png "diagrama de clases")


##  Principios SOLID
[![solid](https://github.com/Jesus-Caballero-Cartuistes/Parcial-1/blob/master/img.png "solid")](https://github.com/Jesus-Caballero-Cartuistes/Parcial-1/blob/master/img.png "solid")


### 1. Principio de Responsabilidad Única (SRP):
Cada clase y microservicio debe tener una sola razón para cambiar. Esto significa que cada clase debe estar encargada de una única tarea o responsabilidad dentro del sistema.

- Clase "AutenticacionUsuario": Su responsabilidad es autenticar usuarios utilizando el microservicio correspondiente.
- Clase "ClientesMicroservicio": Se encarga exclusivamente de gestionar la información de los clientes.
- Clase "GestionProducto": Su única tarea es enviar información al microservicio de productos.
- Clase "GestionUsuario": Responsable de enviar información al microservicio de usuarios.
- Clase "Producto": Representa un producto y sus propiedades, cumpliendo únicamente con la responsabilidad de modelar los productos.
- Clase "RecomendacionProducto": Encargada de enviar información al microservicio de recomendaciones de productos.
- Clase "RecomendacionMicroservicio": Su responsabilidad es procesar y generar recomendaciones de productos.
### 2. Principio de Abierto/Cerrado (OCP):
Las clases deben estar abiertas para la extensión pero cerradas para la modificación. Esto significa que se pueden agregar nuevas funcionalidades sin necesidad de cambiar el código existente.

- Interfaces "Autenticacion" y "Gestion": Permiten la extensión mediante la implementación de nuevas clases que cumplan con estas interfaces sin modificar el código existente.
- Clase "Proveedor" y sus clases hijas: Pueden ser extendidas para agregar nuevos tipos de proveedores sin necesidad de modificar el código existente.
- Microservicios "ProductoMicroservicio", "ClientesMicroservicio" y "RecomendacionMicroservicio": Pueden ser extendidos para agregar nuevas funcionalidades relacionadas con productos, clientes y recomendaciones sin modificar el código existente.
### 3. Principio de Sustitución de Liskov (LSP):
Las clases derivadas deben poder reemplazar a sus clases base sin afectar el comportamiento del programa.

- Clase "Cliente" y "Admin": Pueden ser usadas en lugar de la clase base "Usuario" sin afectar la funcionalidad relacionada con la autenticación y gestión de usuarios.
- Clase "Proveedor" y sus clases hijas: Pueden ser tratadas como instancias de la clase base "Proveedor" sin afectar la lógica de negocio relacionada con la gestión de productos y recomendaciones.
### 4. Principio de Segregación de Interfaces (ISP):
Los clientes no deben verse obligados a depender de interfaces que no utilicen.

Interfaces "Autenticacion" y "Gestion": Están diseñadas específicamente para cada tipo de funcionalidad, de modo que los clientes solo dependan de las interfaces que necesiten para su funcionamiento. Por ejemplo, un cliente que solo necesite autenticación no necesitará depender de la interfaz de gestión y viceversa.
### 5. Principio de Inversión de Dependencias (DIP):
Los módulos de alto nivel no deben depender de los módulos de bajo nivel. Ambos deben depender de abstracciones.

Interfaces "Autenticacion" y "Gestion": Sirven como abstracciones que permiten que los módulos de alto nivel interactúen con los módulos de bajo nivel a través de interfaces, en lugar de depender directamente de implementaciones concretas. Por ejemplo, un cliente que requiere autenticación no necesita conocer los detalles de implementación del microservicio de autenticación, solo interactúa a través de la interfaz correspondiente.

Al seguir estos principios, el diseño del sistema será más flexible, mantenible y escalable, lo que facilitará la incorporación de nuevas funcionalidades y la adaptación a cambios futuros sin necesidad de reescribir gran parte del código existente.
