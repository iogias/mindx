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

# Im using django restframework auth-token

- Create your user via django admin page, and then you can create token or you can create via api
- Endpoint for create token , {{url}}/api-token-auth/ , provide your credentials on body, then you get token

# Notes for JavaScript

```sh
inside your header, add the token that received from auth-token
{ method: "post", headers: { "Content-Type": "application/json", "Authorization": "Token fc017e6e6180acc49d0a3c0cb5a389486ddf9bc3" }

```
