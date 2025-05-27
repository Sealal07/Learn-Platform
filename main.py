from django.contrib.admin.templatetags.admin_list import admin_actions
from django.template.defaultfilters import title

pip install django pillow
django-admin startproject learn_platform
cd learn_platform
django-admin startapp courses
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
admin admin
python manage.py runserver
python manage.py dumpdata courses --indent=2
mkdir courses/fixtures
python manage.py dumpdata courses --indent=2 --output=courses/fixtures/subjects.json
# уникальность
python manage.py loaddata subjects.json
pip freeze > requirements.txt
python manage.py shell

SHELL:
>>> from django.contrib.auth.models import User
>>> from courses.models import Subject, Course, Module
>>> user = User.objects.last()
>>> subject = Subject.objects.last()
>>> c1 = Course.objects.create(subject=subject, owner=user, title='Course 1', slug='course1')
>>> m1 = Module.objects.create(course=c1, title='Module 1')
>>> m1.order


SHELL2:
python manage.py shell
from courses.models import Module
Module.objects.latest('id').id

python -m pip install django-braces
