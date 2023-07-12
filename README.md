## GreenatomTest

This solution used technologies such as: FastApi, PostgreSQL, Tensorflow. To test the functionality of the application it is recommended to add to the url ../docs

### Set Up the app in Windows

>Download the code
```
$ git clone https://github.com/spacefellow/GreenatomTest
Create .dbenv and .dev_env files in root folder
$ cd greenatom
```

>.dev_env contains
```
SECRET_KEY=some secret key
```

>.dbenv contains
```
DB_DRIVER=postgresql
DB_CONNECTOR=asyncpg
DB_USER=user
DB_PASS=pass
DB_HOST=localhost
DB_PORT=5432
DB_NAME=db_name
```

>Install modules VENV
```
$ virtualenv env
$ .\env\Scripts\activate
$ pip install -r requirements.txt
```

>Start the app
```
Create database 'db_name' in PostgreSQL
$ alembic init migrations
$ alembic revision --autogenerate -m "initial"
$ alembic upgrade head
$ uvicorn main:app --reload
```

### Start the app in Docker

>Download the code
```
$ git clone https://github.com/spacefellow/GreenatomTest
Create .dbenv and .dev_env files in root folder
$ cd GreenatomTest
```

>.dev_env contains
```
SECRET_KEY=some secret key
```

>.dbenv contains
```
DB_DRIVER=postgresql
DB_CONNECTOR=asyncpg
DB_USER=user
DB_PASS=pass
DB_HOST=database
DB_PORT=5432
DB_NAME=db_name
```

>Make docker images
```
$ docker-compose build
$ docker-compose up -d
```

>Create database in db container
```
$ docker-compose exec -it database psql —host database -U
$ CREATE DATABASE db_name;
```

>Create alembic migrations in the backend_container and load data into the database
```
$ docker-compose exec -it backend bash
$ alembic init migrations
$ alembic revision --autogenerate -m "initial"
$ alembic upgrade HEAD
```

At this point, the app runs at http://localhost:8000/

### OpenAPI documentation

```
This application implements swagger for documenting endpoints.
The documentation can be accessed via the url http://.../docs
```
