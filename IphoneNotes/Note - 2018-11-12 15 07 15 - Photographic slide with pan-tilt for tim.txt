11/12/18, 3:07 PM

Photographic slide with pan-tilt for timelapse/video

-Arduino
-energy supply 
-screen module
-CBC shield v3 board
-3 motor control module drv8825 or 
-3 motors displacement, rotation and up-down
-timing belt and pulleys correa gt2
-cámara trigger conexión
-sensor de final de carrera mechanical endstop limit switch 

Se debe poder programar:
+lado de inicio L/R
+Recorrido cm
+Tiempo total
+Timelapse
         +Intervalo entre fotos
+hay rotación:
          +fijo
                +Angulo
          +incremental
               +angulo inicial
               +angulo final
               +vuelve a posición inicial
+hay movimiento up-down:
          +fijo
               +ángulo 
          +incremental 
               +Ángulo inicial
               +Angulo final 
               +Vuelve a posición inicial 

                  -90...0...90

                         90
                           0
                       -90

Casi especial que el punto focal este en El Centro 

Se debería conocer la distancia del punto focal para poder calcular el ángulo inicial y final 

                       A
                       |\
                       |  \
                 b    |    \   c
                       |      \
                       |        \
                    C-------B
                           a

               a^2+b^2=c^2
a=recorrido/2
b=distancia al punto focal 
se calcula c=sqrt(a^2+b^2)

Ángulo de C=90
Ángulo de B=cos-1((c^2+a^2-b^2)/2ca)
Ángulo de A=90-B

a=1
b=2
c=sqrt(1+4)=2.236

B=tan-1(1/2.236)=tan-1(0.447)=24.085

A=90-24.085=65.915

Si se comienza por L
Ángulo inicial B y final -B
Si se comienza por R
Ángulo inicial -B y final B




