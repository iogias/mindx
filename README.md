# Create your python environment and install library

```sh
# create python environment
python3 -m venv env
source env/bin/activate

# install requirements
cd konigle
pip3 install -r requirements.txt
```

```sh
# Migrating models
python3 manage.py makemigrations
python3 manage.py migrate

# Create super user for admin access

python3 manage.py createsuperuser

# follow the rest

```
# Notes for JavaScript