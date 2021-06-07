#!bin/bash
#****/sh for alpine

gunicorn -w 4 -b 0.0.0.0:$(WSGI_PORT) --chdir $(PROJECT_DIR)/src Django1.wsgi --timeout 60 --log-level debug --max-requests 10000
