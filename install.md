## DJANGO-BLOGGER

### Setup Postgresql:
* sudo apt-get update
* sudo apt-get install python-pip python-dev libpq-dev postgresql postgresql-contrib
* sudo su - postgres
* psql
* CREATE DATABASE django_blogger;
* CREATE USER blogger WITH PASSWORD 'blogger';
* ALTER ROLE myprojectuser SET client_encoding TO 'utf8';
* ALTER ROLE myprojectuser SET default_transaction_isolation TO 'read committed';
* ALTER ROLE myprojectuser SET timezone TO 'UTC';
* GRANT ALL PRIVILEGES ON DATABASE myproject TO myprojectuser;
* \q
* exit

### Create a virtual environment:
* sudo apt-get install python-virtualenv
* virtualenv project_env
* source ~/project_env/bin/activate

### Use pip to install requirements:
* while virtual environment is active:
* go to requirements.txt location
* pip install -r requirements.txt

### To start a project with a name project_oj:
* git clone https://github.com/RitehWebTeam/django-blogger.git
* django-admin.py startproject --template=django-blogger --extension=py,rst,html,gitignore,sh,bat,conf,json,less project_oj
