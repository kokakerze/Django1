FROM python:3.9

RUN uname -a
RUN apt update && apt install -y --no-install-recommends python-dev python-setuptools

WORKDIR /srv/project
COPY requirements.txt /tmp/requirements.txt
COPY src/ src/

RUN pip install -r /tmp/requirements.txt
CMD ["python", "./src/manage.py", "runserver", "0.0.0.0:8111"]

EXPOSE 8111