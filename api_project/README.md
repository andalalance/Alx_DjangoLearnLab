# api_project (DRF starter)

Commands:
pip install django djangorestframework
cd /home/lance/repos_secondary/Alx_DjangoLearnLab/api_project
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver

API endpoints:
GET  /api/books/          -> list (ListAPIView)
CRUD /api/books_all/      -> router-powered ModelViewSet
POST /api/token-auth/     -> obtain token (username + password)