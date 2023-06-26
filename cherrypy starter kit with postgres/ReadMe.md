# Full Stack Cherrypy with Redis

 Cherrypy webserver
 docker & docker-compose
 redis-sessions, redis-cache
 traefik
 postgres, pgadmin, sqlalchemy
 redis, redis-commander
 alembic migrations
 celery, celery-flower

# ToDOS:

 celery-beat
 cors
 JWT Token
 CI
 Maxmind geoip 

# Alembic usage

alembic init alembic
alembic revision --autogenerate -m "create campaign model" # create the migrations file
alembic upgrade heads  # push the migration to the database


# Celery

celery -A celery_app worker --loglevel=info   # To run the celery app. Run it outside the celery_app folder

# .env file (development)

```
###### Postgres
DB_HOST=localhost
DB_USER=postgres
DB_PASSWORD=johnjose
DB_NAME=tracker2
DB_PORT=5432

###### Redis
REDIS_HOST=localhost
REDIS_PORT=6379
REDIS_DB=0

###### Rabbitmq
RABBIT_HOST=localhost
RABBIT_USER=admin
RABBIT_PASSWORD=johnjose


###### Celery
BACKEND_URL=rpc://
BROKER_URL=amqp://${RABBIT_USER}:${RABBIT_PASSWORD}@${RABBIT_HOST}

###### Postgres

DATABASE_URL=postgresql://${DB_USER}:${DB_PASSWORD}@${DB_HOST}:${DB_PORT}/${DB_NAME}

VITE_APP_API=http://localhost:3000/api
```

# .env file (production)

```
###### Postgres
DB_HOST=db
DB_USER=postgres
DB_PASSWORD=johnjose
DB_NAME=tracker2
DB_PORT=5432

###### Redis
REDIS_HOST=redis
REDIS_PORT=6379
REDIS_DB=0

###### Rabbitmq
RABBIT_HOST=rabbit
RABBIT_USER=admin
RABBIT_PASSWORD=johnjose


###### Celery
BACKEND_URL=rpc://
BROKER_URL=amqp://${RABBIT_USER}:${RABBIT_PASSWORD}@${RABBIT_HOST}
```

###### Postgres
DATABASE_URL=postgresql://${DB_USER}:${DB_PASSWORD}@${DB_HOST}:${DB_PORT}/${DB_NAME}

VITE_APP_API=http://localhost:3000/api
