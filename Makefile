include .env
export $(shell sed 's/=.//' .env)
MANAGE = python src/manage.py
PROJECT_DIR = $(shell pwd)
WSGI_PORT=8000
RUN_COMMAND=gunicorn-run
#RUN_COMMAND=run

run:
	$(MANAGE) runserver 0.0.0.0:$(WSGI_PORT)

celery-run:
	cd src && celery -A Django1 worker -l INFO

celerybeat-run:
	cd src && rm -rf celerybeat.pid && celery -A Django1 beat -l INFO


new-migrations:
	$(MANAGE) makemigrations

new-migrations-acc:
	$(MANAGE) makemigrations account


migrate:
	$(MANAGE) migrate

migrate-acc:
	$(MANAGE) migrate account

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

fillposts:
	$(MANAGE) fill_posts

gen-category:
	$(MANAGE) gen_books_cat

test:
	cd src && pytest --cov=main --cov-report=html --cov-fail-under=40
	open static_content/coverage/index.html

unitest:
	cd src && pytest

dkr-rn:
	docker run --rm -t -d -p 8001:8111 --name ssb ssb:1.0

dkr-bld:
	docker build -t ssb:1.0 .

dkr-st:
	docker container stop ssb

dkr-up-dev:dkr-down
	$(eval RUN_COMMAND=run)
	docker-compose up -d --build
	make copy-static

dkr-up-prod: dkr-down
	$(eval RUN_COMMAND=gunicorn-run)
	docker-compose up -d --build
	make copy-static

dkr-down:
	docker-compose down

dkr-nmigrations:
	docker exec -it ssb-backend $(MANAGE) makemigrations

dkr-migrate:
	docker exec -it ssb-backend $(MANAGE) migrate --noinput

dkr-runserver:
	docker exec -it ssb-backend $(MANAGE) runserver 0.0.0.0.:9000

dkr-ini-env:
	cp .env.example env.my

copy-static:
	docker exec -it ssb-backend python ./src/manage.py collectstatic --noinput
	docker cp ssb-backend:/tmp/static_content/static /tmp/static
	docker cp /tmp/static nginx:/etc/nginx;

dkr-runserver-breakpoint:
	docker exec -it ssb-backend $(MANAGE) runserver 0.0.0.0:9000

urls:
	$(MANAGE) show_urls



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