# Ejercicios Educativa

Esta es una guía para poder ejecutar correctamente cada uno de los seis ejercicios que se plantearon.
  
## Instalación de dependencias

Para poder ejecutar cada uno de los ejercicios, va a ser necesario disponer del intérprete de **Python**, junto con su instalador de paquetes (**pip**), y el motor de DB **MySQL**. Cabe destacar, que las instrucciones referidas a Linux, han sido probadas en la distribución Mint 21.1 Cinnamon.

### Python  

#### Windows

Basta con entrar a [Descargas de Python](https://www.python.org/downloads/windows/) e instalar la versión más reciente del intérprete.

#### Linux

La mayoría de distribuciones, ya incluyen el intérprete de Python, y su gestor de paquetes, instalados.

Para comprobarlo:

```bash
which  python3
#Generalmente el PATH puede encontrarse en:
#/usr/bin/python3
#/usr/local/bin/python3
```

Si **NO** es el caso, procederemos a instalar ambas dependencias:

```bash
sudo  apt-get  update
sudo  apt-get  install  python3.7  python3-pip
```

### MySQL

#### Windows

Se dispone de [MySQL Server](https://dev.mysql.com/downloads/mysql/) para instalar el motor. Se puede complementar con [MySQL Workbench](https://dev.mysql.com/downloads/workbench/), una interfaz gráfica para evitar utilizar las líneas de comando. También se puede descargar directamente el [Instalador](https://dev.mysql.com/downloads/installer/) para elegir de manera personalizada todos los complementos que se van a instalar.

#### Linux

Para instalar el motor de DB:

```bash
sudo  apt  install  mysql-server
```

Comprobamos que el servicio esté activo:

```bash
sudo  systemctl  status  mysql
```

En caso de no estarlo, basta con ejecutar la siguiente línea:

```bash
sudo  systemctl  start  mysql
```

## Preparar para ejecución  

### Clonar repositorio

```bash
git  clone  https://github.com/AlanHoltz/{usuario}@ejercicios-educativa.git
  
#{usuario} es el nombre con el que se está logueado actualmente en Git
```

Nos dirigimos al repositorio:

```bash
cd  /.../ejercicios-educativa
```

### Crear base de datos

En **Windows**, se puede usar directamente MySQL Workbench. Importamos el archivo `db_creation.sql` y lo ejecutamos.

En **Linux**, usamos la terminal para importarlo. Si MySQL Server está recién instalado, lo más probable es que tengamos que loguearnos como usuario root:  

```bash
sudo  su
mysql  -u  root < db_creation.sql
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
