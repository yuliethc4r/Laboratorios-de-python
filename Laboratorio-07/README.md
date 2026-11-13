# ClassroomHub — Laboratorio 7: persistencia con MySQL/MariaDB

Continúa el Laboratorio 6: los recursos ahora son registros de base de datos.

- Modelos `Category` y `Resource` (relación uno a muchos, `on_delete=PROTECT`).
- Migraciones, conexión por `.env` y Django Admin para gestionar el catálogo.
- `/resources/` consulta el ORM con `select_related("category")`.

## Puesta en marcha

Requisitos: Python 3.12 o superior y un servidor MySQL 8.4+ (o MariaDB 10.11+) local.

```bash
python3 -m venv .venv
source .venv/bin/activate        # Windows: .\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
cp .env.example .env             # y escribe tu contraseña real en .env
```

Crea la base y la cuenta de la aplicación (cambia la contraseña por una privada):

```sql
CREATE DATABASE IF NOT EXISTS classroom_hub CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
CREATE USER IF NOT EXISTS 'classroomhub_user'@'127.0.0.1' IDENTIFIED BY 'TU_CONTRASEÑA_PRIVADA';
GRANT ALL PRIVILEGES ON classroom_hub.* TO 'classroomhub_user'@'127.0.0.1';
GRANT ALL PRIVILEGES ON test_classroom_hub.* TO 'classroomhub_user'@'127.0.0.1';
```

```bash
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

## Rutas

| URL | Nombre | Acceso |
|---|---|---|
| `/` | `pages:home` | Público |
| `/resources/` | `pages:resources` | Público |
| `/about/` | `pages:about` | Público |
| `/admin/` | — | Superusuario |

Crea categorías y recursos desde `/admin/` y verifica que aparezcan en `/resources/`.

## Pruebas (10)

```bash
python manage.py test pages
```
Se ejecutan sobre la base descartable `test_classroom_hub`.
