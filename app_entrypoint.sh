#!/bin/bash

RUN cp /etc/nginx/uwsgi_params /var/scat/

uwsgi --http :3031 --chdir /var/scat/ --wsgi-file app/wsgi.py  --socket /tmp/uwsgi.sock  --uid www-data --buffer-size=51200 &

nginx -g "daemon off;"
