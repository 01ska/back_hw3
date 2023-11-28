[program:HW3]
command=/home/ubuntu/django_deploy_app/venv/bin/gunicorn_configuration
user=root
autostart=true
autorestart=true
redirect_stderr=true
stdout_logfile=/home/ubuntu/django_deploy_app/logs/gunicorn-error.log
