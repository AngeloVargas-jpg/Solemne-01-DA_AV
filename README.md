API Hora Oficial de Chile (FastAPI + NTP)

Descripción

Este proyecto consiste en una API desarrollada con FastAPI que entrega la hora oficial de Chile obtenida desde un servidor NTP (ntp.shoa.cl). La aplicación consulta la hora en tiempo real y la expone mediante un endpoint REST en formato JSON.

---

Ejecución local

1. Clonar el repositorio

git clone <URL_DEL_REPOSITORIO>
cd <NOMBRE_DEL_PROYECTO>

2. Instalar dependencias

Usando uv:

pip install uv
uv sync

Alternativa usando pip:

pip install fastapi uvicorn ntplib

3. Ejecutar la aplicación

uvicorn main:app --reload

4. Acceso a la API

Abrir en el navegador:

http://localhost:8000/time

Documentación

http://localhost:8000/docs

---

Ejecución con Docker

1. Construir la imagen

docker build -t fastapi-shoa .

2. Ejecutar el contenedor

docker run -p 8000:8000 fastapi-shoa

3. Acceso a la API

Abrir en el navegador:

http://localhost:8000/time

---

Pruebas de la API

Uso con navegador

Acceder directamente a:

http://localhost:8000/time


Ejemplo de respuesta:

{
  "Hora_Oficial_Chile": "2026-04-05 21:30:00"
}
---

Endpoint disponible

Método| Ruta| Descripción
GET| /time| Obtiene la hora oficial de Chile

---

Notas

- La API requiere conexión a internet para consultar el servidor NTP.
- En caso de fallo del servidor NTP, la API retornará un mensaje de error.

---

Autor

Diego Alvarez
Angelo Vargas
