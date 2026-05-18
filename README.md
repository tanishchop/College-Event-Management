# College Event Management System

[![Python](https://img.shields.io/badge/python-3.8%2B-blue)](https://www.python.org/)
[![Django](https://img.shields.io/badge/django-3.2%2B-green)](https://www.djangoproject.com/)
[![License](https://img.shields.io/badge/license-MIT-lightgrey)](#license)

A lightweight Django application to manage college events, organizers, and schedules. The app provides a desktop-focused UI, user authentication, and an admin panel for easy management.

Features

- Event and schedule management (create/read/update/delete)
- Organizer roles and user registration
- Authentication (login, logout, registration)
- Admin interface for site-wide management
- Small, dependency-light stack using SQLite by default

Quick links

- Events list: `/events/`
- Admin: `/admin/`
- Login: `/accounts/login/`

Table of contents

- [Requirements](#requirements)
- [Local setup (Windows PowerShell)](#local-setup-windows-powershell)
- [Run with Docker](#run-with-docker)
- [Project layout](#project-layout)
- [Testing](#testing)
- [Contributing](#contributing)
- [License](#license)

Requirements

- Python 3.8 or newer
- pip
- (Optional) Docker

Local setup (Windows PowerShell)

1. Create and activate a virtual environment:

```powershell
python -m venv venv
venv\Scripts\Activate.ps1
```

2. Install dependencies:

```powershell
pip install -r requirements.txt
```

3. Apply migrations and create a superuser:

```powershell
python manage.py migrate
python manage.py createsuperuser
```

4. Run the development server:

```powershell
python manage.py runserver
```

Open http://127.0.0.1:8000/ and navigate to `/events/`.

Run with Docker

Build image:

```powershell
docker build -t college-event-app .
```

Run (bind port 8000):

```powershell
docker run -p 8000:8000 college-event-app
```

Notes: the included Dockerfile runs the Django development server. For production you should use a proper WSGI server and a production-grade database.

Project layout

Key folders and files:

- `eventmanager/` — Django project settings and WSGI/asgi entrypoints
- `events/` — main app (models, views, templates, forms, admin)
- `requirements.txt` — Python dependencies
- `manage.py` — Django management entrypoint

Testing

Run the Django test suite (fast local tests):

```powershell
python manage.py test
```

