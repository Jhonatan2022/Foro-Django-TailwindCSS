# Forum With Django And React <a href="mailto:florezj328@gmail.com"> <img src="https://img.shields.io/badge/Gmail-red?style=for-the-badge&logo=gmail&logoColor=white" width="80px" alt="Jhonattan Florez"/> </a>

## Requisitos previos

- [Python](https://www.python.org/downloads/)
- [Node](https://nodejs.org/es/download/)
- [DB Browser for SQLite](https://sqlitebrowser.org/dl/)

## Webs de utilidad

- [Django](https://www.djangoproject.com/)
- [Tailwind CSS](https://tailwindcss.com/)
- [Django Tailwind](https://django-tailwind.readthedocs.io/en/latest/installation.html)

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

# Comprobando el backend de Users con Postman

- [Postman](https://www.postman.com/)

## Comprobamos el registro de usuarios

![](img/Register%20User.png)

## Comprobamos el login de usuarios

![](img/Login.png)

## Comprobamos el actualizado de datos

1. Copiamos el access token que nos devuelve el login y lo pegamos en el campo de autorización de Postman
   ![](img/Token%20User.png)
   ![](img/Put%20Desde%20Postman.png)

## Comprobamos el perfil de usuario

![](img/User%20Profile%20Postman.png)

## Comprobamos el obtener solo un usuario

![](img/Solo%20Un%20Usuario%20Postman.png)

## Comprobamos el obtener todos los usuarios

![](img/Obtener%20Todos%20Los%20Usuarios%20Postman.png)

# Comprobamos el backend de Blogs con Postman

## Comprobamos el crear un Blog Post

![](img/Create%20Post.png)

## Comprobamos el obtener todos los Blog Post

![](img/Get%20All%20Posts.png)

## Comprobamos el obtener un Blog Post

![](img/Get%20Alone%20Post.png)

## Comprobamos el actualizar un Blog Post

![](img/Update%20Post.png)

## Comprobamos el borrar un Blog Post

![](img/Delete%20Post.png)

# Comprobamos el backend de Comentarios con Postman

![](img/Comment%20Postman.png)
![](img/Forum%20Posts.png)
