# Full Stack Cherrypy with Redis

Cherrypy webserver
docker
docker-compose
redis-sessions
redis-cache
traefik
postgres docker
pgadmin
redis-docker
redis-commander
sql-alchemy
alembic migrations
computed fields
celery
celery-flower

ToDOS:

celery-beat
cors
JWT Token
CI
geoip

# Alembic usage

alembic init alembic
alembic revision --autogenerate -m "create campaign model" # create the migrations file
alembic upgrade heads  # push the migration to the database


# Celery

celery -A celery_app worker --loglevel=info   # To run the celery app. Run it outside the celery_app folder



