# Proyecto FastAPI

Esta es una aplicación FastAPI con la siguiente estructura:

```
.
├── app/
│   ├── core/              # Configuración y utilidades
│   ├── api/               # Endpoints y rutas
│   │   └── v1/            # Versionado
│   ├── models/            # Modelos de DB
│   ├── schemas/           # Esquemas Pydantic
│   ├── services/          # Lógica de negocio
│   ├── repositories/      # Acceso a datos (DB)
│   ├── dependencies.py    # Inyección de dependencias
│   └── main.py            # Entrypoint
├── tests/                 # Pruebas unitarias/integración
├── alembic/               # Migraciones de DB
├── requirements.txt
└── .env
```

## Instalación

1. Crear entorno virtual:
   ```bash
   python -m venv venv
   source venv/bin/activate
   ```

2. Instalar dependencias:
   ```bash
   pip install -r requirements.txt
   ```

3. Ejecutar la aplicación:
   ```bash
   uvicorn app.main:app --reload
   ```
