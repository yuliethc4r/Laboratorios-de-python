# ClassroomHub — Laboratorio 8: autenticación, sesiones y permisos

Continúa el Laboratorio 7 sin cambiar la base de datos.

- Registro (`UserCreationForm`), login y logout por POST con CSRF.
- Panel privado `/dashboard/` con contador de visitas en sesión.
- Grupo `Catalog reviewers` con el permiso `pages.view_resource` y vista de revisión (403 sin permiso).
- Reto: `/dashboard/summary/` con totales obtenidos del ORM.

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
| `/resources/review/` | `pages:resource-review` | Autenticado + `view_resource` (403 sin permiso) |
| `/about/` | `pages:about` | Público |
| `/accounts/signup/` | `pages:signup` | Anónimo |
| `/accounts/login/` | `pages:login` | Anónimo |
| `/accounts/logout/` | `pages:logout` | POST |
| `/dashboard/` | `pages:dashboard` | Autenticado |
| `/dashboard/summary/` | `pages:dashboard-summary` | Autenticado |

## Grupo de revisores (shell)

```python
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from pages.models import Resource

ct = ContentType.objects.get_for_model(Resource)
view_perm = Permission.objects.get(content_type=ct, codename="view_resource")
reviewers, _ = Group.objects.get_or_create(name="Catalog reviewers")
reviewers.permissions.add(view_perm)
```
Asigna el grupo a una cuenta desde `/admin/`. El registro público nunca concede privilegios.

## Pruebas (28)

```bash
python manage.py test pages
```
