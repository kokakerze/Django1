#include .env
#export $(shell sed 's/=.//' .env)
MANAGE = python src/manage.py
PROJECT_DIR = $(shell pwd)
WSGI_PORT=8081

run:
	$(MANAGE) runserver 0.0.0.0:8000


new-migrations:
	$(MANAGE) makemigrations


migrate:
	$(MANAGE) migrate

lint:
	flake8 .

check:
	$(MANAGE) check

check-migrations:
	$(MANAGE) makemigrations --check --dry-run


shell:
	$(MANAGE) shell_plus --print-sql


createsuperuser:
	$(MANAGE) createsuperuser

gunicorn-run:
	gunicorn -w 4 -b 0.0.0.0:$(WSGI_PORT) --chdir $(PROJECT_DIR)/src Django1.wsgi --timeout 60 --log-level debug --max-requests 10000


collect-static:
	$(MANAGE) collectstatic
#	python manage.py startapp main
#	pip install django
#	pip install Faker
#	pip install django_extensions
#	pip install django-debug-toolbar
#	pip install flower
#	brew install rabbitmq

#logs in nginx
#tail -f /usr/local/var/log/nginx/error.log
#tail -f /usr/local/var/log/nginx/access.log