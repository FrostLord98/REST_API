Este repo contiene una REST API que permite realizar un CRUD si se tiene la autenticacion mediante JWT.

Para iniciar la DB, que es PostgreSQL, se debe agregar un .env con los datos que solicita psycopg2 que son database, host, port, user, password y una variable key en el mismo .env que se utilizara como secret key para JWT

Las rutas del CRUD son las siguientes:

La ruta /register  usando el metodo post permite registrar un nuevo usuario, un ejemplo de solicitud seria el siguiente.

username = "foo"
password ="123"
email = "f@f.f"

Con esos datos usando el endpoint /register dara como resultado esta respuesta del servidor {"payload":"success"} que indica que se agrego un nuevo usuario en la base de datos previamente configurada.

La ruta /login usando el metodo post permite logear al usuario y de esta forma generar un JWT para ser usado por otras rutas, un ejemplo usando el usuario anterior ya que en este ejemplo "esta registrado".

username ="foo"
password="123"

Estos datos enviados a la ruta /login daran como respuesta el bearer token que sera descrito como token de ahora en adelante.

La ruta /user usando el metodo get permite mostrar los datos del usuario registrado que se encuentras encriptados en el token que se genero en la ruta anterior.

Al enviar el token como header nos dara las siguiente respuesta: {"user":los datos del usuario,"payload":"success"}.

la ruta /user usando el metodo put nos permite actualizar los datos  del usuario autenticado al pasarle el token y los datos a cambiar.

username ="echo"
email="e@e.e"
token

Asi se ve una solicitud de  /user con metodo put y el resultado de esta ruta seria {"data":un nuevo token,"payload":"success"}.
En este caso se genera un token usando los nuevos datos del usuario registrado.

Y finalmente tenemos la ruta /user con el metodo delete, que le permitira al usuario borrar su propia cuenta.
La solicitud seria similar al /user con metodo get, ya que utiliza el token del usuario para autorizar el borrado de su cuenta, y nos mostraria lo siguiente:
{"payload":"success"}

Esto nos indica que se elimino la cuenta con exito.







