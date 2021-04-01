run:
	python manage.py runserver


make-migrate:
	python manage.py makemigrations


migrate:
	python manage.py migrate

lint:
	flake8 .

