# Mattilda API

Mattilda API es una aplicación construida con FastAPI para gestionar colegios, estudiantes y facturas.

## Requisitos

* Tener Python 3.10 o superior instalado (puedes verificar con `python3 --version`).
* Tener la herramienta `make` instalada (ya viene incluida en la mayoría de sistemas Linux y macOS).

Este proyecto ha sido diseñado para ejecutarse en sistemas operativos tipo Unix, como Linux o macOS. No es compatible con Windows a menos que se utilice WSL (Windows Subsystem for Linux).

## Instalación y ejecución

Para crear el entorno virtual, instalar dependencias y ejecutar la aplicación, simplemente corre:

```
make run_all
```

Este comando realiza automáticamente lo siguiente:

1. Crea un entorno virtual en la carpeta `venv/`.
2. Instala los paquetes necesarios listados en `requirements.txt`.
3. Ejecuta el servidor de desarrollo usando Uvicorn.
4. Abre en el navegador la documentación automática de la API.

Puede ver otros comandos disponibles en el Makefile ejecutando:

```
make help
```

## Acceso a la documentación

Una vez ejecutada la aplicación, puedes acceder a la documentación automática de la API en los siguientes enlaces:

* Swagger UI: [http://localhost:8000/docs](http://localhost:8000/docs)
* Redoc: [http://localhost:8000/redoc](http://localhost:8000/redoc)

Desde alli podra hacer peticiones a la API, ver los esquemas de los modelos y probar los endpoints ingresando datos de prueba.

## Estructura del proyecto

```
mattilda-test/
├── app/
│   ├── main.py
│   ├── models.py
│   ├── schemas.py
│   ├── database.py
│   ├── crud.py
│   └── routers/
│       ├── schools.py
│       ├── students.py
│       └── invoices.py
├── requirements.txt
├── Makefile
└── README.md
```

## Activación manual del entorno (opcional)

Si necesitas trabajar dentro del entorno virtual manualmente, puedes activarlo con:

```
source venv/bin/activate
```

Y luego puedes ejecutar la app con:

```
uvicorn app.main:app --reload
```

## Limpieza del entorno

Para eliminar el entorno virtual creado:

```
rm -rf venv/
```
