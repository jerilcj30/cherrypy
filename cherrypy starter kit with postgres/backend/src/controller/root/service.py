import cherrypy
from celery_app.tasks import add

class Service(object):
    def __init__(self):
        pass

    @property
    def db(self):
        return cherrypy.request.db
    
    def get_service(self):

        # celery task
        result = add.delay(1,2)
        print(result.result)
        return {"result": result}

        # Storing to redis
        cherrypy.request.rdb.set("key3", "mango1")          
        return "This is GET service jeril jose chaliss apple"

    def post_service(self):        
        return "This is POST service"
    
    def put_service(self):
        return "This is PUT Service"

    def delete_service(self):
        return "This is Delete Service"