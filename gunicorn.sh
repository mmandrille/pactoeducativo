#!/bin/bash
cd /opt/pactoeducativo
source venv/bin/activate
cd /opt/pactoeducativo/pactoeducativo
gunicorn pactoeducativo.wsgi -t 600 -b 127.0.0.1:8000 -w 6 --user=servidor --group=servidor --log-file=/opt/pactoeducativo/pactoeducativo/gunicorn.log 2>>/opt/pactoeducativo/pactoeducativo/gunicorn.log

