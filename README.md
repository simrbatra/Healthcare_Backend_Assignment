
# Healthcare Backend (Django + DRF + PostgreSQL)

This is a simple, human-written Django backend for a healthcare app implementing:
- JWT Authentication (djangorestframework-simplejwt)
- Patient, Doctor models and CRUD APIs
- Patient-Doctor mappings (assign/remove)
- PostgreSQL via environment variables
- Basic validation and permission checks (authenticated access where required)

## Setup (locally)

1. Create a virtualenv and activate it.
2. Install requirements:
   ```bash
   pip install -r requirements.txt
   ```
3. Create a `.env` file at project root with these variables:
   ```env
   SECRET_KEY=your_django_secret_key
   DEBUG=True
   DB_NAME=your_db_name
   DB_USER=your_db_user
   DB_PASSWORD=your_db_password
   DB_HOST=localhost
   DB_PORT=5432
   ```
4. Run migrations and create a superuser:
   ```bash
   python manage.py migrate
   python manage.py createsuperuser
   ```
5. Run the server:
   ```bash
   python manage.py runserver
   ```

## APIs

Authentication:
- POST /api/auth/register/  -> { name, email, password }
- POST /api/auth/login/     -> returns JWT tokens (access/refresh) using simplejwt

Patients (authenticated):
- POST /api/patients/
- GET  /api/patients/
- GET  /api/patients/<id>/
- PUT  /api/patients/<id>/
- DELETE /api/patients/<id>/

Doctors (authenticated to create/update/delete; GET list is public):
- POST /api/doctors/
- GET  /api/doctors/
- GET  /api/doctors/<id>/
- PUT  /api/doctors/<id>/
- DELETE /api/doctors/<id>/

Mappings (authenticated):
- POST /api/mappings/  -> assign doctor to patient (patient_id, doctor_id)
- GET  /api/mappings/  -> list mappings
- GET  /api/mappings/<patient_id>/ -> get doctors for a patient
- DELETE /api/mappings/<id>/ -> remove mapping

"# Healthcare_Backend_Assignment" 
