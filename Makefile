run:
	python manage.py runserver


new-migrations:
	python manage.py makemigrations


migrate:
	python manage.py migrate

lint:
	flake8 .

check:
	python manage.py check

check-migrations:
	python manage.py makemigrations --check --dry-run


shell:
	python manage.py shell_plus --print-sql


createsuperuser:
	python manage.py createsuperuser


#	python manage.py startapp main
#	pip install django
#	pip install Faker
#	pip install django_extensions
#	pip install django-debug-toolbar
#	pip install flower
#	brew install rabbitmq