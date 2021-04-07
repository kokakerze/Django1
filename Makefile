run:
	python manage.py runserver


make-migration:
	python manage.py makemigrations


migrate:
	python manage.py migrate

lint:
	flake8 .

