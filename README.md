# FincaScore
Pagina web para calificar fincas cafeteras

## 🚀 Correr el proyecto en local

Sigue estos pasos para configurar y ejecutar el proyecto en tu entorno local:

### 1️⃣ Clonar el repositorio  
Primero, clona el proyecto desde el repositorio de GitHub y accede a la carpeta del proyecto:  
```bash
git clone git@github.com:JHONATAN9A/FincaScore.git
cd FincaScore
```
### 2️⃣ Instalar PostgreSQL
Para que el proyecto funcione correctamente, necesitas instalar PostgreSQL. Puedes descargarlo desde postgresql.org.

## 3️⃣ Crear y activar un entorno virtual  
Crea un entorno virtual para manejar las dependencias del proyecto sin afectar otros proyectos en tu sistema:  

```bash  
python -m venv env  
```  

Luego, actívalo según tu sistema operativo:  

- **En macOS/Linux:**  
  ```bash  
  source env/bin/activate  
  ```  
- **En Windows:**  
  ```bash  
  env\Scripts\activate  
  ```  

---  

## 4️⃣ Instalar dependencias  
Con el entorno virtual activado, instala las dependencias del proyecto:  

```bash  
pip install --upgrade pip  
pip install -r requirements.txt  
```  

---  

## 5️⃣ Configurar las variables de entorno  
Crea un archivo `.env` en la raíz del proyecto:  

```bash  
touch .env  
```  

Luego, edítalo y agrega la siguiente configuración:  

```env  
DB_NAME=""
DB_USER=""
DB_PASSWORD=""
DB_HOST=""
DB_PORT=
 
```  

---  

## 6️⃣ Aplicar migraciones (opcional)  
Ejecuta los siguientes comandos para crear la estructura de la base de datos:  

```bash  
python manage.py makemigrations  
python manage.py migrate  
```  

---  

## 7️⃣ Crear un superusuario (opcional)  
Si necesitas acceso al panel de administración de Django, crea un superusuario con:  

```bash  
python manage.py createsuperuser  
```  

Sigue las instrucciones y proporciona un nombre de usuario, correo y contraseña.  

---  

## 8️⃣ Iniciar el servidor de desarrollo  
Ejecuta el siguiente comando para levantar el servidor:  

```bash  
python manage.py runserver  
```  

El proyecto estará disponible en `http://127.0.0.1:8000/`. 🎉🚀

<<<<<<< HEAD


>>>>>>> b5f2e0d89f867e34fa64266aa8e0675e83e49e9e


