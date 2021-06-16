FROM python:3.9 AS builder_python_ssb

RUN uname -a
RUN apt update && apt install -y --no-install-recommends python-dev python-setuptools

WORKDIR /srv/project
COPY requirements.txt requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

FROM builder_python_ssb as builder

# This prevents Python from writing out pyc files
ENV PYTHONDONTWRITEBYTECODE 1
# This keeps Python from buffering stdin/stdout
ENV PYTHONUNBUFFERED 1
ENV SERVER_MODE=prod
#[wsgi,celery,celerybeat]
ENV BACKEND_SERVER=wsgi

COPY src/ src/
COPY commands/ commands/
RUN chmod +rx -R commands
COPY ./Makefile Makefile

RUN useradd -ms /bin/bash admin
RUN chown -R admin:admin /srv/project
RUN chmod 755 /srv/project
USER admin



#EXPOSE 8000

#CMD ["python", "./src/manage.py", "runserver", "0.0.0.0:8000"]
#CMD bash -C './commands/wsgi_dev.sh'

