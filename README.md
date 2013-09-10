UINGaming.com
=============

# Development Environment Setup

## Dependecias:
	 1 - MySQL-server
	 2 - MySQL-client
	 3 - Memcached
	 4 - python-memcache
	 5 - python-pylibmc
	 6 - py-bcrypt v0.4
	 7 - Django 1.5.2
	 8 - Node
	 9 - coffeescript
	
##Instruciones de Instalacion:
    
Primero corremos el siguiente comando. Durante la instalacion de mysql-server, se le pedira una contrasenia para el usuario root de la base de datos. RECUERDE ESA CONTRASEÑA, le sera requerida para configurar la base de datos
     
    
	sudo apt-get install mysql-server mysql-client memcached python-pylibmc python-memcache python-dev python-pip python-mysqldb python-software-properties python g++ make                    
    
     
Una vez instaladas las dependecias basicas, procedemos a instalar la biblioteca de hasheo de contraseñas utilizado python-pip
     
	sudo pip install py-bcrypt
     
Ahora instalaremos Django ejecutando el siguiente comnado:
    
	sudo pip install Django==1.5.2
     
Verificar que los procesos memcached y mysqld esten corriendo utilizando el comando pgrep. Si no estan corriendo iniciarlos, o reiniciar la pc para que se inicien al bootear
    
	pgrep memcached 
	pgrep mysqld

Ahora instalemos node ejecutando el siguiente comnado:

	sudo add-apt-repository ppa:chris-lea/node.js
	sudo apt-get update
	sudo apt-get install nodejs coffeescript
	
En el directorio donde se encuentra el archivo 'package.json' correr el siguiente comando:

		sudo npm install
		
Se instalaron todas las dependecias. Ahora hay que configurar la base de datos.

## Configuracion de la base de datos:

Ingresar al cliente mysql utilizando el siguiente comando. Se le pedira la contrasenia del usuario root, especificada en el primer paso de instalacion.
    
	mysql -u root -p
     
Una vez ingresado al cliente mysql, correremos las siguientes sentencias especificando usuario y contrasenia que correspondan
      
	CREATE USER 'usuario'@'localhost' IDENTIFIED BY 'contraseña';  # Crea el usuario con acceso a la DB local
	GRANT ALL PRIVILEGES ON *.* TO 'usuario'@'localhost' WITH GRANT OPTION;  # Le da permisos al usuario creado
	CREATE USER 'usuario'@'%' IDENTIFIED BY 'contraseña';  # Crea el usuario con acceso a la DB remota
	GRANT ALL PRIVILEGES ON *.* TO 'usuario'@'%' WITH GRANT OPTION;  # Le da permisos al usuario creado
    
Para que funcione correctamente deben crearse tanto el usuario local como remoto.
    
Ahora procederemos a realizar lo mismo paro para el usuario admin. Este usuario usara la aplicacion web para realizar operaciones en la base de datos. Dejar la contraseña tal y como está ('admin')
      
	CREATE USER 'admin'@'localhost' IDENTIFIED BY 'admin';  
	GRANT ALL PRIVILEGES ON *.* TO 'admin'@'localhost' WITH GRANT OPTION;  
	CREATE USER 'admin'@'%' IDENTIFIED BY 'admin';  
	GRANT ALL PRIVILEGES ON *.* TO 'admin'@'%' WITH GRANT OPTION;
      
Ahora procederemos a crear la base de datos. En nuestro caso corremos el siguiente comando y luego salimos de mysql con el comando exit.
    
	CREATE DATABASE UINGaming;
        
Para administrar la base de datos creada correr el siguiente comando. Ingresar el usuario y contrasenias creadas en los pasos anteriores.
        
	mysql -u usuario -p  UINGaming
	
# Correr el proyecto:
Antes de correr el proyecto tenemos que asegurarnos de que la dirección donde tenemos todos los archivos estaticos(CSS, imagenes, JavaScript) y todos los templates (archivos .html) esté agregada a la ruta de busqueda en el archivo de configuración de Django. Para esto, abrimos debug.py dentro de la carpeta settings y buscamos las variables TEMPLATE_DIRS y STATICFILES_DIRS y agregamos nuestra direccion absoluta. ES IMPORTANTE que sea absoluta, ya que Django no toma rutas relativas (lamentablemente)
    
La primera vez que se corre el proyecto y tambien siempre que se cambian las clases del modelo que tienen representacion en una base de datos, se debe correr el comando:
     
	./manage syncdb
     
El archivo manage.py se encuentra en el root del proyecto.

Para inicializar el server corremos el siguiente comando. El server correra en localhost:8000 y para entrar en la consola de administracion de Django hay que ingresar a http://localhost:8000/admin
   
	./manage runserver
     
Para crear una nueva aplicacion (lease un nuevo modulo de la aplicacion que estamos creado, ej. authentication) corremos el siguiente comando:
   
	./manage startapp
     
Para correr pruebas unitarias en general o de una aplicacion(ver punto anterior) en particular se corre el siguiente comando. Si no se especifica la aplicacion, se corren todas las pruebas.
   
	./manage test [aplicacion]
	
# Correr frontend testing server

Debe ejecutarse el siguiente comando e ingresar a la siguiente direccion en el explorador: http://localhost:3000

	./runserver.sh
