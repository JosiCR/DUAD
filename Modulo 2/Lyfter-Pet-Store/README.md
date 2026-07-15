# Lyfter Pawstore:

PawStore es una tienda virtual de productos para mascotas desarrollada con HTML, CSS y JavaScript. La aplicación permite a los usuarios registrarse, iniciar sesión, explorar un catálogo de productos, consultar información detallada, administrar un carrito de compras y completar pedidos.

También incluye un panel de administración que permite gestionar el inventario y consultar el historial de ventas realizadas.

---

## Funcionalidades

### Autenticación

- Registro de nuevos usuarios.
- Validación de campos obligatorios.
- Validación del formato del correo electrónico.
- Validación de contraseñas.
- Confirmación de contraseña.
- Inicio de sesión para clientes.
- Inicio de sesión para administradores.
- Persistencia de la sesión mediante `localStorage`.
- Cierre de sesión con confirmación.
- Restricción de páginas según el estado de la sesión.
- Restricción del panel administrativo según el rol del usuario.

### Catálogo de productos

- Visualización dinámica de productos.
- Búsqueda de productos por nombre.
- Filtrado de productos por categoría.
- Visualización de imagen, nombre, categoría, precio y stock.
- Página individual con información detallada de cada producto.
- Mensaje cuando no se encuentran productos.
- Pantalla de inicio de sesión requerido para usuarios sin una sesión activa.

### Carrito de compras

- Agregar productos al carrito.
- Aumentar la cantidad de un producto.
- Disminuir la cantidad de un producto.
- Eliminar productos del carrito.
- Validación del stock disponible.
- Cálculo automático de subtotales.
- Cálculo automático del total de la compra.
- Persistencia del carrito mediante `localStorage`.
- Estado visual para el carrito vacío.

### Proceso de compra

- Formulario con información de entrega.
- Resumen de los productos seleccionados.
- Visualización de cantidades y subtotales.
- Cálculo del total del pedido.
- Confirmación de la compra.
- Actualización automática del stock.
- Registro de la venta.
- Limpieza automática del carrito.
- Página de compra completada.
- Visualización de los productos comprados.
- Visualización del total pagado.

### Panel de administración

- Acceso exclusivo para usuarios administradores.
- Visualización del inventario.
- Creación de productos.
- Edición de productos.
- Eliminación de productos.
- Confirmación antes de eliminar un producto.
- Visualización del historial de ventas.
- Información del cliente.
- Fecha y hora de cada compra.
- Productos y cantidades vendidas.
- Total de cada pedido.

---

## Tecnologías utilizadas

- HTML5
- CSS3
- JavaScript
- Axios
- RESTful API
- Local Storage
- Flexbox
- CSS Grid

---

## Estructura del proyecto

```text
PawStore/
│
├── assets/
│   └── images/
│
├── css/
│   ├── admin.css
│   ├── auth.css
│   ├── cart.css
│   ├── catalog.css
│   ├── checkout.css
│   ├── edit-product.css
│   ├── main.css
│   └── product.css
│
├── js/
│   ├── admin/
│   │   ├── admin.js
│   │   └── edit.product.js
│   │
│   ├── auth/
│   │   ├── login.js
│   │   └── register.js
│   │
│   ├── cart/
│   │   ├── cart.js
│   │   └── checkout.js
│   │
│   ├── catalog/
│   │   ├── catalog.js
│   │   └── product.js
│   │
│   └── services/
│       ├── authService.js
│       ├── cartService.js
│       └── productService.js
│
├── pages/
│   ├── admin.html
│   ├── cart.html
│   ├── catalog.html
│   ├── checkout.html
│   ├── edit-product.html
│   ├── index.html
│   ├── login.html
│   ├── product.html
│   ├── purchase-completed.html
│   └── register.html
│
└── README.md
```

---

## Cómo ejecutar el proyecto

1. Clonar el repositorio:

```bash
git clone URL_DEL_REPOSITORIO
```

2. Abrir la carpeta del proyecto en Visual Studio Code.

3. Instalar la extensión **Live Server** si todavía no está instalada.

4. Abrir el siguiente archivo:

```text
pages/index.html
```

5. Hacer clic derecho sobre el archivo.

6. Seleccionar la opción:

```text
Open with Live Server
```

7. La aplicación se abrirá automáticamente en el navegador.

> Se recomienda ejecutar el proyecto mediante Live Server para evitar problemas relacionados con las rutas de los archivos.

---

## Registro de clientes

Para crear una cuenta:

1. Abrir la página de registro.
2. Ingresar un nombre.
3. Ingresar un correo electrónico válido.
4. Crear una contraseña de al menos 8 caracteres.
5. Confirmar la contraseña.
6. Presionar el botón **Registrarse**.
7. Iniciar sesión con las credenciales registradas.

---

## Credenciales del administrador

Para acceder al panel administrativo se pueden utilizar las siguientes credenciales:

```text
Correo: admin@lyfter.com
Contraseña: admin123
```

Después de iniciar sesión, aparecerá la opción **Administrador** en la barra de navegación.

---

## Conexión con la API

PawStore utiliza Axios para realizar solicitudes HTTP a una API REST.

La API se utiliza durante el registro de usuarios para simular la comunicación con un servicio externo.

Ejemplo de solicitud:

```javascript
const response = await axios.post("https://api.restful-api.dev/objects", user);
```

La aplicación utiliza programación asíncrona mediante `async` y `await` para esperar la respuesta del servidor antes de continuar con el proceso.

También implementa manejo de errores mediante bloques `try` y `catch`, lo que permite controlar errores de conexión o respuestas inesperadas y mostrar mensajes comprensibles al usuario.

---

## Uso de Local Storage

La aplicación utiliza `localStorage` para conservar información importante directamente en el navegador.

Los datos almacenados incluyen:

- Usuario registrado.
- Usuario administrador.
- Sesión actual.
- Productos.
- Carrito de compras.
- Último pedido realizado.
- Historial de ventas.

Las principales claves utilizadas son:

```text
registeredUser
adminUser
currentUser
products
cart
lastOrder
orders
```

---

## Decisiones técnicas y justificación

Durante el desarrollo de PawStore se tomaron diferentes decisiones técnicas con el objetivo de mantener una estructura organizada, reducir la repetición de código, facilitar el mantenimiento y conservar correctamente la información utilizada por la aplicación.

### Uso de HTML, CSS y JavaScript

La aplicación fue desarrollada utilizando HTML, CSS y JavaScript sin frameworks.

HTML se utiliza para definir la estructura y el contenido de las páginas. CSS administra la apariencia visual y la adaptación de la interfaz. JavaScript controla las validaciones, la interacción del usuario y la lógica relacionada con la autenticación, los productos, el carrito, las compras y la administración.

Se utilizaron estas tecnologías porque permiten separar claramente la estructura, la presentación y el comportamiento de la aplicación. El uso de JavaScript sin frameworks también evita agregar dependencias y complejidad innecesarias para las necesidades actuales de PawStore.

### Organización por carpetas

Los archivos se organizaron en diferentes carpetas según su función:

- `pages` contiene las páginas HTML.
- `css` contiene los estilos de la aplicación.
- `js` contiene la lógica desarrollada con JavaScript.
- `assets` contiene las imágenes y otros recursos visuales.

Esta organización permite localizar los archivos con mayor facilidad y evita mezclar páginas, estilos, lógica y recursos dentro de una misma carpeta.

También facilita agregar nuevas funcionalidades sin desorganizar la estructura existente.

### Separación del código JavaScript

El código JavaScript se dividió según la responsabilidad de cada funcionalidad:

- `auth` contiene la lógica relacionada con el registro y el inicio de sesión.
- `catalog` contiene la lógica para mostrar, buscar y filtrar productos.
- `cart` contiene la lógica relacionada con el carrito y el proceso de compra.
- `admin` contiene la lógica para administrar productos y visualizar ventas.
- `services` contiene funciones reutilizables relacionadas con la autenticación, los productos y el carrito.

Esta separación evita crear un único archivo demasiado extenso y permite modificar una funcionalidad sin afectar innecesariamente otras partes de la aplicación.

### Uso de archivos de servicios

Se crearon los siguientes archivos de servicios:

```text
authService.js
productService.js
cartService.js
```

Estos archivos contienen funciones que pueden utilizarse desde diferentes páginas.

Por ejemplo, las funciones relacionadas con crear, editar, eliminar y obtener productos se encuentran en `productService.js`, mientras que las funciones relacionadas con agregar, modificar o eliminar productos del carrito se encuentran en `cartService.js`.

Esta separación reduce la repetición de código y permite que cada archivo tenga una responsabilidad específica.

### Uso de una API REST

PawStore utiliza una API REST externa durante el registro de usuarios.

La solicitud se realiza mediante Axios:

```javascript
const response = await axios.post("https://api.restful-api.dev/objects", user);
```

La API permite enviar información a un servicio externo y recibir una respuesta sin necesidad de implementar un servidor propio.

Después de recibir una respuesta válida, la información necesaria del usuario se guarda localmente para permitir el inicio de sesión dentro de la aplicación.

### Uso de Axios

Se utilizó Axios para realizar solicitudes HTTP porque proporciona una sintaxis clara para enviar información y acceder a las respuestas del servidor.

También facilita la identificación de errores según la respuesta recibida y funciona de manera sencilla con `async` y `await`.

### Uso de programación asíncrona

Las solicitudes a la API utilizan `async` y `await`.

La programación asíncrona es necesaria porque una solicitud puede tardar en recibir una respuesta. La aplicación debe esperar el resultado antes de confirmar si una operación fue exitosa o mostrar un mensaje de error.

El uso de `async` y `await` permite mantener este proceso organizado y facilita la lectura del flujo de ejecución.

### Manejo de errores

Las solicitudes utilizan bloques `try` y `catch`.

El manejo de errores evita que una falla de conexión o una respuesta inesperada detenga la ejecución de la aplicación.

Los errores se convierten en mensajes comprensibles para informar al usuario sobre lo ocurrido.

### Uso de Local Storage

Se utilizó `localStorage` para almacenar información directamente en el navegador.

Esta decisión permite conservar datos sin implementar una base de datos propia. La información permanece disponible después de recargar la página o cerrar y volver a abrir el navegador.

`localStorage` se utiliza para conservar:

- Usuarios.
- Sesión actual.
- Productos.
- Carrito.
- Último pedido.
- Historial de ventas.

### Uso de roles

Los usuarios poseen un rol:

```javascript
role: "customer"
```

o:

```javascript
role: "admin"
```

Los roles permiten diferenciar los permisos disponibles dentro de la aplicación.

Los clientes pueden consultar productos, utilizar el carrito y realizar compras. El administrador puede acceder al panel de inventario, gestionar productos y consultar el historial de ventas.

Antes de permitir el acceso al panel administrativo, la aplicación verifica que exista una sesión activa y que el usuario tenga el rol `admin`.

### Persistencia del carrito

El carrito se almacena en `localStorage`.

Esta decisión evita que los productos seleccionados desaparezcan cuando el usuario recarga la página.

Cada producto conserva su información y la cantidad seleccionada hasta que sea eliminado o se complete la compra.

### Validación del stock

El sistema verifica el stock cuando el usuario agrega productos al carrito y vuelve a comprobarlo antes de confirmar la compra.

La segunda validación evita completar una compra cuando la cantidad disponible ya no es suficiente.

Después de completar el pedido, la cantidad comprada se descuenta automáticamente del inventario.

Por ejemplo:

```text
Stock inicial: 50

Cantidad comprada: 4

Stock actualizado: 46
```

Esto permite mantener el inventario actualizado y evita vender más unidades de las disponibles.

### Separación entre el último pedido y el historial de ventas

La aplicación utiliza dos elementos diferentes:

```text
lastOrder
orders
```

`lastOrder` almacena los productos de la compra más reciente y permite mostrarlos inmediatamente en la página de compra completada.

`orders` conserva todas las ventas realizadas y permite mostrarlas en el historial del panel administrativo.

Los datos se separaron porque cumplen funciones diferentes. El último pedido se utiliza para mostrar el resultado inmediato de la compra, mientras que el historial conserva todas las ventas realizadas.

### Actualización del inventario

Después de confirmar una compra, la aplicación busca cada producto adquirido y descuenta la cantidad comprada de su stock.

La actualización se realiza antes de guardar la venta y vaciar el carrito.

Esto permite que el catálogo y el panel administrativo muestren la cantidad disponible actualizada después de cada compra.

### Separación de los estilos CSS

Los estilos se dividieron en diferentes archivos:

```text
main.css
auth.css
catalog.css
product.css
cart.css
checkout.css
admin.css
edit-product.css
```

`main.css` contiene los estilos generales compartidos entre varias páginas.

Los demás archivos contienen estilos relacionados con páginas o secciones específicas.

Esta separación evita crear un único archivo CSS demasiado extenso y facilita localizar y modificar los estilos de una sección sin afectar innecesariamente las demás.

### Uso de Flexbox y CSS Grid

Se utilizaron Flexbox y CSS Grid para organizar los elementos de la interfaz.

Flexbox se utiliza principalmente para alinear elementos en filas o columnas, como la barra de navegación, los formularios, los controles del carrito y diferentes secciones administrativas.

CSS Grid se utiliza para organizar elementos que necesitan una distribución en varias filas y columnas, como las tarjetas del catálogo.

Ambas herramientas permiten crear distribuciones flexibles sin depender de posiciones fijas.

### Uso de unidades relativas

Se utilizaron principalmente unidades relativas como:

```css
rem
%
```

Estas unidades permiten que los tamaños mantengan una relación más consistente con el tamaño base del documento y el espacio disponible.

También facilitan la adaptación de los elementos a diferentes tamaños de pantalla.

### Diseño adaptable

Se utilizaron consultas de medios para modificar la distribución de algunos elementos cuando el espacio disponible es menor.

Ejemplo:

```css
@media (max-width: 48rem){

}
```

También se agregó desplazamiento horizontal a las tablas administrativas para evitar que el contenido se salga de la pantalla.

Estas decisiones permiten conservar la legibilidad y facilitar la navegación en diferentes tamaños de pantalla.

---

## Flujo principal de la aplicación

```text
Inicio
↓
Registro
↓
Inicio de sesión
↓
Catálogo
↓
Detalle del producto
↓
Carrito
↓
Finalizar compra
↓
Compra completada
↓
Actualización del inventario
↓
Registro de la venta
↓
Panel administrativo
```

---

## Autor

Desarrollado por **Josias Nuñez**.