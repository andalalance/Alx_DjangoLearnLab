# django-models Project

This project demonstrates the use of Django models, including ForeignKey, ManyToMany, and OneToOne relationships. It also implements user authentication, role-based access control, and custom permissions.

## Project Structure

```
django-models
├── manage.py
├── django_models
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── relationship_app
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── forms.py
│   ├── serializers.py
│   ├── tests.py
│   └── migrations
│       └── __init__.py
├── accounts
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── forms.py
│   ├── tests.py
│   └── migrations
│       └── __init__.py
├── templates
│   ├── registration
│   │   ├── login.html
│   │   └── logout.html
│   └── relationship_app
│       ├── list.html
│       └── detail.html
├── static
│   └── relationship_app
│       └── styles.css
├── requirements.txt
├── .env.example
├── pytest.ini
└── README.md
```

## Setup Instructions

1. **Clone the repository:**
   ```
   git clone <repository-url>
   cd django-models
   ```

2. **Create a virtual environment:**
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies:**
   ```
   pip install -r requirements.txt
   ```

4. **Run migrations:**
   ```
   python manage.py migrate
   ```

5. **Create a superuser:**
   ```
   python manage.py createsuperuser
   ```

6. **Run the development server:**
   ```
   python manage.py runserver
   ```

## Features

- **Models:** Demonstrates ForeignKey, ManyToMany, and OneToOne relationships through various models in `relationship_app`.
- **User Authentication:** Implements login, logout, and registration functionalities in the `accounts` app.
- **Role-Based Access Control:** Custom user roles are defined in the `UserProfile` model.
- **Custom Permissions:** Permissions can be assigned to different user roles for accessing various parts of the application.

## Usage

- Access the application at `http://127.0.0.1:8000/`.
- Admin panel is available at `http://127.0.0.1:8000/admin/` for managing models and users.

## License

This project is licensed under the MIT License.