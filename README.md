# Sistema de Recomendación de Productos

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

- Clase "AutenticacionUsuario": Su única responsabilidad es autenticar usuarios utilizando el microservicio de autenticación correspondiente. Esta clase no debe preocuparse por otras tareas como la gestión de productos o clientes.

- Clase "ClientesMicroservicio": Se encarga exclusivamente de gestionar la información de los clientes, como la creación, actualización y eliminación de registros de clientes. No tiene la responsabilidad de autenticar usuarios ni de recomendar productos.

- Clase "GestionProducto": Su única tarea es enviar información relacionada con productos al microservicio correspondiente. No se encarga de otras operaciones como la gestión de usuarios o la generación de recomendaciones.

- Clase "GestionUsuario": Responsable de enviar información relacionada con usuarios al microservicio correspondiente. Su única responsabilidad es gestionar la información de usuarios, como la creación de nuevos usuarios o la actualización de sus datos.

- Clase "Producto": Representa un producto y sus propiedades. Su única responsabilidad es modelar los productos, como su nombre, categoría, precio, etc. No se encarga de operaciones relacionadas con la gestión de usuarios o la autenticación.

- Clase "RecomendacionProducto": Encargada de enviar información al microservicio de recomendaciones de productos. Su única responsabilidad es generar recomendaciones de productos basadas en el historial de preferencias del usuario y otras métricas relevantes.

- Clase "RecomendacionMicroservicio": Su responsabilidad es procesar y generar recomendaciones de productos. No se encarga de otras tareas como la autenticación de usuarios o la gestión de clientes.

Al seguir el Principio de Responsabilidad Única, cada clase y microservicio del sistema realiza una tarea específica y claramente definida. Esto hace que el sistema sea más fácil de entender, mantener y extender, ya que cada componente tiene una responsabilidad clara y no está sobrecargado con funcionalidades adicionales que no le corresponden.
### 2. Principio de Abierto/Cerrado (OCP):
Las clases deben estar abiertas para la extensión pero cerradas para la modificación. Esto significa que se pueden agregar nuevas funcionalidades sin necesidad de cambiar el código existente.

- Interfaces "Autenticacion" y "Gestion": Estas interfaces definen las funciones que deben cumplir las clases que las implementan. Al definir interfaces claras y específicas, se permite que nuevas clases que cumplan con estas interfaces puedan ser agregadas al sistema sin modificar el código existente. Por ejemplo, si se desea agregar un nuevo tipo de autenticación o gestión de productos, solo se necesitaría crear una nueva clase que implemente la interfaz correspondiente.

- Clase "Proveedor" y sus clases hijas: La clase base "Proveedor" y sus clases hijas (por ejemplo, "ProveedorSeguros", "ProveedorTarjetasCredito", etc.) están diseñadas para ser extendidas para agregar nuevos tipos de proveedores. Esto se logra definiendo una clase base común con comportamiento genérico y luego creando subclases específicas para cada tipo de proveedor. De esta manera, se puede agregar un nuevo tipo de proveedor simplemente creando una nueva subclase sin modificar el código existente.

- Microservicios "ProductoMicroservicio", "ClientesMicroservicio" y "RecomendacionMicroservicio": Estos microservicios están diseñados para ser extendidos para agregar nuevas funcionalidades relacionadas con productos, clientes y recomendaciones, respectivamente. Por ejemplo, si se desea agregar una nueva funcionalidad al microservicio de productos, como la gestión de inventario, se puede crear una nueva clase o microservicio que extienda la funcionalidad existente sin modificar el código existente.

Al seguir el Principio de Abierto/Cerrado, el diseño del sistema permite agregar nuevas funcionalidades de manera flexible y sin riesgo de introducir errores en el código existente. Esto facilita la adaptación del sistema a nuevos requisitos y cambios en el negocio sin comprometer su integridad o estabilidad.
### 3. Principio de Sustitución de Liskov (LSP):
Las clases derivadas deben poder reemplazar a sus clases base sin afectar el comportamiento del programa.

- Clase "Cliente" y "Admin": Estas clases derivan de la clase base "Usuario". De acuerdo con el Principio de Sustitución de Liskov, cualquier lugar en el código donde se espera una instancia de la clase base "Usuario" debería poder recibir una instancia de las clases derivadas "Cliente" o "Admin" sin que el comportamiento del programa se vea afectado. Esto significa que las clases derivadas deben heredar correctamente el comportamiento y las propiedades de la clase base.

- Clase "Proveedor" y sus clases hijas: Similar al caso anterior, las clases derivadas de la clase base "Proveedor" deben poder ser usadas en lugar de la clase base sin afectar el comportamiento del programa. Por ejemplo, si hay un método que espera recibir un objeto de tipo "Proveedor", debería poder recibir cualquier subtipo de "Proveedor" (por ejemplo, "ProveedorSeguros", "ProveedorTarjetasCredito", etc.) sin problemas.

Garantizar que las clases derivadas puedan ser sustituidas por sus clases base sin cambios en el comportamiento del programa ayuda a mantener la coherencia y la consistencia en el diseño del sistema. Esto facilita la reutilización del código y promueve una mayor flexibilidad y extensibilidad del sistema, ya que nuevas clases derivadas pueden ser introducidas sin impactar en el funcionamiento de las partes existentes del sistema.
### 4. Principio de Segregación de Interfaces (ISP):
Los clientes no deben verse obligados a depender de interfaces que no utilicen.

- Interfaces "Autenticacion" y "Gestion": Estas interfaces están diseñadas de manera que los clientes puedan depender únicamente de los métodos que necesitan para sus funcionalidades específicas. Por ejemplo, un cliente que solo requiere funcionalidades de autenticación no necesita depender de los métodos relacionados con la gestión de productos.

- Clase "AutenticacionUsuario": Implementa la interfaz "Autenticacion", lo que significa que proporciona solo los métodos necesarios para autenticar usuarios. De esta manera, los clientes que necesiten funcionalidades de autenticación pueden depender de esta clase sin preocuparse por otros aspectos del sistema.

- Clase "GestionProducto" y "GestionUsuario": Implementan la interfaz "Gestion", lo que les permite proporcionar funcionalidades específicas relacionadas con la gestión de productos y usuarios respectivamente. Esto asegura que los clientes que necesiten interactuar con productos o usuarios solo dependan de las interfaces relevantes sin verse obligados a depender de funcionalidades que no utilizan.

### 5. Principio de Inversión de Dependencias (DIP):
Los módulos de alto nivel no deben depender de los módulos de bajo nivel. Ambos deben depender de abstracciones.

- Interfaces "Autenticacion" y "Gestion": Estas interfaces son abstracciones que definen los contratos que deben cumplir los módulos de bajo nivel (microservicios) encargados de implementar la funcionalidad concreta. Los módulos de alto nivel (clases que las utilizan) dependen de estas interfaces en lugar de depender directamente de las implementaciones concretas.

- Microservicios: Los microservicios "ProductoMicroservicio", "ClientesMicroservicio" y "RecomendacionMicroservicio" implementan las interfaces ("GestionProducto", "GestionUsuario", etc.). De esta manera, los módulos de alto nivel que utilizan estas funcionalidades interactúan a través de abstracciones en lugar de depender directamente de las implementaciones concretas de los microservicios.

Al aplicar el Principio de Inversión de Dependencias, se reduce el acoplamiento entre los diferentes módulos del sistema, lo que facilita la modificación, extensión y mantenimiento del código. Además, se promueve la reutilización de código y se facilita la sustitución de implementaciones concretas sin afectar a otros componentes del sistema.

Siguiendo estos principios, el diseño del sistema será más flexible, mantenible y escalable, lo que facilitará la incorporación de nuevas funcionalidades y la adaptación a cambios futuros sin necesidad de reescribir gran parte del código existente.
