## GreenatomTest

This solution used technologies such as: FastApi, PostgreSQL, Tensorflow.

### Set Up the app

>Download the code
```
$ git clone https://github.com/spacefellow/greenatom
Create .dbenv and .dev_env files in root folder
$ cd xakaton
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

At this point, the app runs at http://127.0.0.1:8000/

### OpenAPI documentation

```
This application implements swagger for documenting endpoints.
The documentation can be accessed via the url http://.../docs
```
