run:
	python src/manage.py runserver


new-migrations:
	python src/manage.py makemigrations


migrate:
	python src/manage.py migrate

lint:
	flake8 .

check:
	python src/manage.py check

check-migrations:
	python src/manage.py makemigrations --check --dry-run


shell:
	python src/manage.py shell_plus --print-sql


createsuperuser:
	python src/manage.py createsuperuser


#	python manage.py startapp main
#	pip install django
#	pip install Faker
#	pip install django_extensions
#	pip install django-debug-toolbar
#	pip install flower
#	brew install rabbitmq