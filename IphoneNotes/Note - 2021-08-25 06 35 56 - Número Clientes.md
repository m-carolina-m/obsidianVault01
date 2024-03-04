8/25/21, 6:35 AM

Número Clientes
Inventario 
Entradas
Salidas 


Wcompra

Terminar lo de los gráficos en el app
Modificar base de datos con valores x 10
Generar app y subirlo a la nube

[https://youtube.com/playlist?list=PLC3y8-rFHvwg2RBz6UplKTGIXREj9dV0G](https://youtube.com/playlist?list=PLC3y8-rFHvwg2RBz6UplKTGIXREj9dV0G)


Netframework
Suspender 


Crear un proyecto vacío, configurar lo básico 
Copiar ese proyecto y en el nuevo proyecto ir agregando partes y si funcionan copiarlo 
Y trabajar en el siguiente, etc 
La idea es si toca deshacer algo lo que hay es que regresar al punto que queremos 
Hay que mantener un historial de que se hizo en cada punto 

Angular:
1-Create project with css and routing 
ng new “name” —routing 

1.1-To run:
Ng serve-O


Make the folders for storing everything:
Components, models, services, 
[https://blog.adnanhalilovic.com/technologies/angular/scalable-angular-structure/](https://blog.adnanhalilovic.com/technologies/angular/scalable-angular-structure/)[
](https://blog.adnanhalilovic.com/technologies/angular/scalable-angular-structure/)
Build shared components 
[https://blog.adnanhalilovic.com/technologies/angular/creating-reusable-components-in-angular/](https://blog.adnanhalilovic.com/technologies/angular/creating-reusable-components-in-angular/)

2-Components and routing:
2.1-Components creation:
Ng g c /components/“name” 
2.2-Our components:
Login 
Registration
Sales 
Inventory 
Purchases 
Finance 

3-Routing:
App.routing.module.ts 
Add the different routes by adding the path and the component and also importing the component
Add the default route for the app

4-UI for components 
Add the html and css for each component, no js to improve speed

4.1-Custom components:
Before we star css
[https://youtu.be/vncch9-1kPE](https://youtu.be/vncch9-1kPE)
[https://youtu.be/bn-DQCifeQQ](https://youtu.be/bn-DQCifeQQ)
[https://youtu.be/vQAvjof1oe4](https://youtu.be/vQAvjof1oe4)
[https://youtu.be/-st14lUQD3U](https://youtu.be/-st14lUQD3U)
[https://youtu.be/3T_Jy1CqH9k](https://youtu.be/3T_Jy1CqH9k)
[https://youtu.be/KrPz_wmBsAE](https://youtu.be/KrPz_wmBsAE)
[https://youtu.be/SLjHSVwXYq4](https://youtu.be/SLjHSVwXYq4)

Do it responsive 
[https://youtu.be/QBfblbmTTF4](https://youtu.be/QBfblbmTTF4)
[https://youtu.be/fm3dSg4cxRI](https://youtu.be/fm3dSg4cxRI)
[https://youtu.be/9e-lWQdO-DA](https://youtu.be/9e-lWQdO-DA)

Set typography 
[https://youtu.be/6ardZEhjvV0](https://youtu.be/6ardZEhjvV0)
[https://youtu.be/zUMAjJ88NJ0](https://youtu.be/zUMAjJ88NJ0)[
](https://youtu.be/zUMAjJ88NJ0)Smooth scrolling
[https://youtu.be/MNNr7TU7XcU](https://youtu.be/MNNr7TU7XcU)

4.1.1- Build the grid
[https://youtu.be/m04RkJwzFgE](https://youtu.be/m04RkJwzFgE)[
](https://youtu.be/m04RkJwzFgE)[https://youtu.be/_lEkD8IGkwo](https://youtu.be/_lEkD8IGkwo)
4.1.2-Build the cards 
[https://youtu.be/51DbAwcmqD8](https://youtu.be/51DbAwcmqD8)
[https://youtu.be/5DEq5cWNYt8](https://youtu.be/5DEq5cWNYt8)
4.1.3-Build the list and pagination 
[https://youtu.be/svhnI9sKUDI
](https://youtu.be/svhnI9sKUDI)[https://youtu.be/lMBa7gLWyO4](https://youtu.be/lMBa7gLWyO4)
4.1.4-Add the graphs bars, lines, doughnut, histogram, gauge 

4.2-Set each component UI

Login UI 
[https://youtu.be/Wi6yaOtNPPE](https://youtu.be/Wi6yaOtNPPE)


5-Build the Navbar and Sidebar [
](https://youtu.be/KrPz_wmBsAE)[https://youtu.be/8QKOaTYvYUA](https://youtu.be/8QKOaTYvYUA)
Add Nav bar 
[https://youtu.be/B-eM50GBB1Y](https://youtu.be/B-eM50GBB1Y)[
](https://youtu.be/KrPz_wmBsAE)
Add hamburger button 
[https://youtu.be/KRpdier1D-0](https://youtu.be/KRpdier1D-0)


Add Css only styling
[https://youtu.be/svhnI9sKUDI](https://youtu.be/svhnI9sKUDI)[
](https://youtu.be/svhnI9sKUDI)
Add side bar 
[https://youtu.be/xkKjrH3pRfg](https://youtu.be/xkKjrH3pRfg)

Change navigation bar on scroll
[https://youtu.be/RxnV9Xcw914](https://youtu.be/RxnV9Xcw914)

Add elements fade on scroll
[https://youtu.be/huVJW23JHKQ](https://youtu.be/huVJW23JHKQ)

6-Services:
6.1-Creation 
App.module.ts add httpclientmodule to the imports array
Ng g s /services/“name”
6.2-Connect the service to the component 
At the component.ts import the service and inject it 

6.3-Our Services:
Login 
Registration 
Sales
Inventory 
Purchases 
Finance 
...


7-Add Cors to the node js server 


8- Add Dark/Light themes 
[https://youtu.be/QtuLN0lNb-Y](https://youtu.be/QtuLN0lNb-Y)[
](https://youtu.be/QtuLN0lNb-Y)Color scheme
[https://youtu.be/mq8LYj6kRyE](https://youtu.be/mq8LYj6kRyE)
[https://youtu.be/Ab9pHqhsfcc](https://youtu.be/Ab9pHqhsfcc)

9-Add Lazy loading
[https://youtu.be/AActXSWxsRo](https://youtu.be/AActXSWxsRo)
[https://youtu.be/mC93zsEsSrg](https://youtu.be/mC93zsEsSrg)

10-

————
Free we hosting
Netlify 
Firebase 
Aws
Heroku 
Github
Vercel
Azure 

Htmlcheatsheet.com
Htmlcheatsheet.com/css
Grid.malven.co
Flexbox.malven.co
Overapi.com/JavaScript


grid.layoutit.com
loading.io/flexbox
griddy .io
mycssbuilder.com
Csslayout.io


<input> pattern: for text field pattern
pattern=“[A-Za-z]{8}”
8 letters, no numbers no special characters 


Shadows.brumm.at
Css-grid-generator.netlify.app

Clamp() for font size relative to screen size and 

Design mobile first:
Set default properties for items small screens and an exception for big screens 
.btn{
    padding: 5px;
}
@media only screen and {min-width: 768px){    
    padding: 10px;
}
——————-
SASS:
Variables 
Nested syntax 
Mixins 

———-
Absolute=positions an element relative to it’s parent’s position 

Relative=relative positions an element relative to it’s own current position 

———-
Chrome extensions:
Css viewer 
Color pick eye dropper 
Whatfont   Or   Fontninja
Json viewer 
Dimensions 


————-

Archery
Shooting
Swimming 
Canoe 
Diving 
Gymnastics

————
Navbar  with a gradient and sliding names
Footer waves 
Sidebar bounce 

Crear un trigger en la bd que cada vez que se genere información en la BD la procesé y la envie a una BD temporal que sea la que se consulte con el api, así se podrían reducir los tiempos de consulta y la información repetida

Crear consultas que traigan toda la información de la página y no por bloques para evitar hacer demasiadas consultas al api 

Cards con glassmorphims en dark y sólidas en light

Table that transfer to cards for mobile
With table hover effect 

[https://event.webinarjam.com/go/live/6/0nmk1bpc9tqt7kl](https://event.webinarjam.com/go/live/6/0nmk1bpc9tqt7kl)

Db-> Heroku or Helio host
Api-> Netlify with aws functions 
Front end->Github or pantheon 
Ip-> freedns.afraid.org

Name: Farmacia La Torre
Username: flatorreandina

Freedom->custom domain 


Comprar en Usa:
Pesas de agua
4 toner 85a
1 toner 12a 
3 Pendrive 
4 Sdd
Dron
Celu, con 3 protectores, el forro y cargador 
1 cable hdmi 
1 audífonos 
Portátil 
4 ventiladores 
1 fuente de poder 750W o más 
Memoria para la portátil y para la pc blanca 

Comprar aquí:
8 tarjetas Rx580 8Gb

