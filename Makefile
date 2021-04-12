run:
	python manage.py runserver


new-migrations:
	python manage.py makemigrations


migrate:
	python manage.py migrate

lint:
	flake8 .
