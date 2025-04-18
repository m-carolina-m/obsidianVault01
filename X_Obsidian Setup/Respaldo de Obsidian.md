1.-Para lograr la sincronización de la portatil y el iphone se implemento un respaldo a través de KOOFR, ambos equipos se sincronizan cada 5 minutos para garantizar que la información este actualizada.

Se utiliza la cuenta de mcarolinam@gmail.com 


2-La portátil además respalda en github al cerrar la aplicación, con un archivo .bat que contiene lo siguiente:
@echo off

cd c://users/MCM/Documents/ObsidianVault
git pull origin master
pause

start /wait obsidian://open?vault=ObsidianVault

git add .
git commit -m "update MCM-LPT"
git push origin master
pause


3.-Por seguridad se usa una llave ssh y po tanto hay que copiar el directorio ./ssh que las contiene