import os
from celery import Celery
from dotenv import load_dotenv

if os.path.exists('/.dockerenv'):
    print("Inside Docker")
else:
    env_path = '../.env'
    # Load variables from .env file
    load_dotenv(dotenv_path=env_path)

BACKEND_URL = os.getenv('BACKEND_URL')
BROKER_URL = os.getenv('BROKER_URL')

app = Celery('celery_app',
             broker=BROKER_URL,
             backend=BACKEND_URL,
             include=['celery_app.tasks'])