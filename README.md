# Forum With Django And React <a href="mailto:florezj328@gmail.com"> <img src="https://img.shields.io/badge/Gmail-red?style=for-the-badge&logo=gmail&logoColor=white" width="80px" alt="Jhonattan Florez"/> </a>

## Requisitos previos
* [Python](https://www.python.org/downloads/)
* [Node](https://nodejs.org/es/download/)
* [DB Browser for SQLite](https://sqlitebrowser.org/dl/)

---
## Pasos a seguir

```sh
# Clonar el repositorio
git clone https://github.com/Jhonatan2022/Foro-Django-TailwindCSS.git
```

```sh
# Movernos a la carpeta del proyecto
cd .\Foro-Django\
```
```sh
# Crear un entorno virtual
virtualenv env
```

```sh
# Damos permisos en powershell para ejecutar el archivo de activacion
# Ejecutamos powerShell como administrador y ponemos:
Set-ExecutionPolicy RemoteSigned
```
```sh
# Activamos el entorno virtual
env/Scripts/activate
```
```sh
# Instalamos los requerimientos de django
pip install -r requirements.sh
```
```sh
# Nos movemos a la carpeta del frontend
cd .\frontend\
```
```sh
# Instalamos los requerimientos de react
npm install
```

--- 

## Pasos para correr el aplicativo

```sh
# Nos movemos a la carpeta principal (foro django)
# Corremos el servidor de django
python manage.py runserver
```

```sh
# Nos movemos a la carpeta del frontend y corremos el servidor de react
cd .\frontend\
npm start
```
![](img/Forum%20Posts.png)