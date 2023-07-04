# Ejercicios Educativa

Esta es una guía para poder ejecutar correctamente cada uno de los seis ejercicios que se plantearon.
  
## Instalación de dependencias

Para poder ejecutar cada uno de los ejercicios, va a ser necesario disponer del intérprete de **Python**, junto con su instalador de paquetes (**pip**), y el motor de DB **MySQL**. Cabe destacar, que las instrucciones referidas a Linux, han sido probadas en la distribución Mint. Puede que sea necesario instalar manualmente el creador de entornos virtuales para concentrar la instalación de las librerías a usar, dependiendo el sistema operativo.

### Python  

#### Windows

Basta con entrar a [Descargas de Python](https://www.python.org/downloads/windows/) e instalar la versión más reciente del intérprete.

#### Linux

La mayoría de distribuciones, ya incluyen el intérprete de Python, y su gestor de paquetes, instalados.

Para comprobarlo:

```bash
which python3
#Generalmente el PATH puede encontrarse en:
#/usr/bin/python3
#/usr/local/bin/python3
```

Si **NO** es el caso, procederemos a instalar ambas dependencias:

```bash
sudo apt-get update
sudo apt-get install python3.7 python3-pip
```

Adicionalmente, tenemos que instalar el generador de entornos virtuales:

```bash
sudo apt-get install python3.10-venv
```

### MySQL

#### Windows

Se dispone de [MySQL Server](https://dev.mysql.com/downloads/mysql/) para instalar el motor. Se puede complementar con [MySQL Workbench](https://dev.mysql.com/downloads/workbench/), una interfaz gráfica para evitar utilizar las líneas de comando. También se puede descargar directamente el [Instalador](https://dev.mysql.com/downloads/installer/) para elegir de manera personalizada todos los complementos que se van a instalar.

#### Linux

Para instalar el motor de DB:

```bash
sudo apt install mysql-server
```

Comprobamos que el servicio esté activo:

```bash
sudo systemctl status mysql
```

En caso de no estarlo, basta con ejecutar la siguiente línea:

```bash
sudo systemctl start mysql
```

## Preparar para ejecución  

### Clonar repositorio

```bash
git clone https://github.com/AlanHoltz/{usuario}@ejercicios-educativa.git
  
#{usuario} es el nombre con el que se está logueado actualmente en Git
```

Nos dirigimos al repositorio:

```bash
cd /.../ejercicios-educativa
```

### Crear base de datos

En **Windows**, se puede usar directamente MySQL Workbench. Importamos el archivo `db_creation.sql` y lo ejecutamos.

En **Linux**, usamos la terminal para importarlo. Si MySQL Server está recién instalado, lo más probable es que tengamos que loguearnos como usuario root:  

```bash
sudo su
mysql -u root < db_creation.sql
```

### Inicializar variables de entorno  

Vamos a crear un archivo `.env`, utilizado para poder acceder a las credenciales necesarias para operar con la base de datos.

Las variables usadas, están especificadas en el archivo `.env.example`, aunque sin los valores seteados. Estos mismos, pueden encontrarse en el archivo que usamos para crear la base de datos (`db_creation.sql`), ya que también, se agrega un nuevo usuario.

Entonces, el contenido de `.env` debería quedar finalmente así:

```
DB_USER = *********
DB_PASSWORD = *********
```

### Generar entorno virtual

Para poder instalar los paquetes necesarios, una muy buena herramienta, son los entornos virtuales, para ahorrarnos conflictos entre las distintas versiones de dichos paquetes.

Creamos y ejecutamos el entorno virtual de la siguiente manera:

En **Windows**:

```bash
py -m venv .venv
.venv\Scripts\activate
```

En **Linux**:

```bash
python3 -m venv .venv
. .venv/bin/activate
```

Una vez dentro del mismo, vamos a instalar los paquetes desde el archivo `requirements.txt`, de esta forma:

```bash
pip install -r requirements.txt
# O 
pip3 install -r requirements.txt
```

Ya estamos en condiciones para ejecutar y probar todos los ejercicios.

## Ejecución de ejercicios

Los ejercicios se encuentran en `.../ejercicios-educativa/src/python`. Cada uno, puede ejecutarse de la siguiente manera:

```bash
py eX.py
# O 			#X=1,2,3,4,5,6
python3 ex.py
```

Si bien todos los ejercicios, se pueden ejecutar de la misma forma, el **e6**, queda a la espera de argumentos.

### Ejercicio 6 (Inscribir usuario a un curso)

Este ejercicio trabaja con argumentos opcionales (no posicionales). Si ejecutamos el mismo, sin especificar ninguna bandera, podremos ver las diferentes opciones:

```bash
py e6.py
# O 
python3 e6.py
```

```bash
usage: e6.py [-h] [-m | -i | -e] [-u USER] [-c COURSE]

options:
  -h, --help            Muestra este mensaje
  -m, --mostrar         Mostrar lista de inscripciones
  -i, --inscribir       Inscribir
  -e, --eliminar        Eliminar
  -u USER, --usuario USER
                        Usuario a inscribir/eliminar de una inscripción
  -c COURSE, --curso COURSE
                        Curso donde inscribir/eliminar la inscripción del usuario
```

#### Ejemplos de uso

Mostrar lista de inscripciones de los usuarios a los distintos cursos:

```bash
py e6 -m
# O
python3 e6 -m
```
Inscribir el usuario con ID 1 al curso de ID 1:

```bash
py e6 -i -u 1 -c 1
# O
python3 e6 -i -u 1 -c 1
```

Eliminar la inscripción del usuario con ID 3 al curso de ID 5:

```bash
py e6 -e -u 1 -c 1
# O
python3 e6 -e -u 1 -c 1
```

## Lenguaje Perl

Si deseamos ejecutar los ejercicios implementados con el lenguaje Perl, adicionalmente a lo hecho con anterioridad, debemos instalar algunas dependencias más.

### Instalar Dependencias

Por defecto, todos los sistemas operativos tipo **UNIX** vienen con el intérprete de Perl integrado, por lo que no hace falta instalarlo manualmente.

En **Windows** basta con descargar el [Entorno de Perl para Windows](https://strawberryperl.com/), elegir la arquitectura adecuada e instalarlo.

### Paquetes necesarios para Perl

Se require la instalación de los siguientes paquetes, utilzando CPAN:

```bash
cpan LWP::UserAgent
cpan JSON
cpan DBI
cpan DBD:mysql
```

### Ejecución de ejercicios

Todos los ejercicios se encuentran en `.../ejercicios-educativa/src/perl`. Cada uno, puede ejecutarse de la siguiente manera:

```bash
perl eX.pm #X=1,2,3,4,5,6
```