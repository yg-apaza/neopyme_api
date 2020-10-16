# Pymes API

## Installation
There is the complete list of packages required by the project (Ubuntu)
```
$ sudo apt-get install build-essential libssl-dev libffi-dev python-dev python python-virtualenv python-pip python3-venv libfreetype6 libfreetype6-dev pkg-config npm postgresql-client postgresql postgresql-contrib postgresql-server-dev-9.x git python3-dev
```
*Notes:*
- You can use postgres 10
- Python version: Python 3.7.9

## Configure packages

### Postgres

```
$ sudo su postgres -c psql

postgres$ create user <user> with password '<password>';

postgres$ create database <database> owner <user> encoding 'UTF8' LC_COLLATE = 'en_US.UTF-8' LC_CTYPE = 'en_US.UTF-8';
```

#### Only for local purposes to use fabric

```
postgres$ alter user <user> with superuser;
```

Edit the `/etc/postgresql/9.x/main/pg_hba.conf` file as root user:

```
local all postgres trust

local all all trust
```

Restart the service

```
$ /etc/init.d/postgresql restart
```

## Configure the project
### Create a virtualenv

```
$ python3.7 -m venv pyme_env
```

This command will create a new folder with the name `pyme_env`

### Clone the project

First verify your SSH Keys on Github configuration

```
$ git clone git@github.com:MilaPacompiaM/pyme_api.git
```

### Activate your enviroment
Inside the `pyme_env` folder run the following command

```
$ source bin/activate
```

After this you will see the virtualenv name in your prompt. i.e.:

```
(pyme_env) $
```

### Install requirements
```
(pyme_env)$ cd pyme-api

(pyme_env)$ pip install -r dev_requirements.txt
```

### Setting up environment variables for project

For environment variables configuration, you will need a .env file in the parent directory of the current folder. Replace secret key.

```
(pyme_env) $ cp .env.example .env
```

### Run the project

Once you have everything ok, you can run the project.

```
(pyme_env) $ ./manage.py check

(pyme_env) $ ./manage.py migrate

(pyme_env) $ ./manage.py runserver
```

### Run tests

Run test:

```
(pyme_env) $ ./manage.py test
```

## Init data
### Create a superuser

Run in project folder

```
(pyme_env) $ ./manage.py createsuperuser
```

Fill with data requested.
