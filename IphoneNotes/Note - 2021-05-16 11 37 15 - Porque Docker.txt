5/16/21, 11:37 AM

Porque Docker?
-permite independizarse del os 
-cada componente de puede independizar en un contenedor
-se tiene que configurar solo una vez el ambiente
-se puede distribuir una sola aplicación que sea independiente de OS
-los contenedores utilizan Linux
-a diferencia de una VM los contenedores todos usa el Mismo OS 
-utilizan menos espacio en disco y utilizan menos memoria y tomen menos tiempo de inicio, pueden compartir recursos e información 
-

Fuente de contenedores:
Docker hub -> hub.docker.com
Docker 

Que son contenedores:
Son imágenes, paquetes de una aplicación. Contienen todas la configuración necesaria para ejecutar una instrucción 
Y debe funcionar en cualquier máquina que tenga Docker 
El contenedor ejecuta una acción y luego sale 

Hay 2 ediciones de Docker: 
Community edition -> gratis 
Enterprise edition -> paga

En Windows/MAC: se pueden instalar de dos maneras 
1-VM
2-Docker environment 

Comandos:
Docker run ... correr contenedor 
   -d detached running mode (background)
   :[tag] corre una versión diferente a la actual “latest”
    -it ... corre atach e interactivo o sea interactúa con el usuario
    -p ... Mapea el puerto de la máquina con el del contenedor ->172.17.0.2:5000, permite que cada contenedor pueda funcionar en diferentes puertos 
Docker atach ... reattached a detached container using the first characters of that container identifier 
Docker ps ....  list contenedor
    -a lista los Contedores que están corriendo
Docker stop .... parar contenedor
Docker rm .... remueve contenedor de memoria 
Docker images ... lista de imágenes
Docker rim ... remueve imágenes de memoria hay que asegurarse que no hay contenedores utilizando
Docker pull ... descarga una imagen de un contenedor
Docker exec... ejecuta un comando sobre un contenedor que esté corriendo





Web server:
Node express

Database:
Mongo

Messaging:
Reddit 


Orchestration: 


