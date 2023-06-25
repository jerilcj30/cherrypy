import cherrypy
import os
from marshmallow import ValidationError
from src.controller.root.service import Service
from src.controller.root.dto.index import RequestDto
import cherrys

__all__ = ["Root"]

# Configure the RedisSession class for session handling
cherrypy.lib.sessions.RedisSession = cherrys.RedisSession

class Root(object):
    exposed = True

    @cherrypy.tools.accept(media='text/plain')
    def GET(self):
        cherrypy.session['something'] = "jeril"
        return Service.get_service(self)

    @cherrypy.tools.json_in()
    @cherrypy.tools.json_out()
    def POST(self):
        author = cherrypy.session.get('something', None)
        print(author)
        name_values = cherrypy.request.json

        # Validate the Request JSON data
        try:
            schema = RequestDto()
            validated_data = schema.load(name_values)
            return Service.post_service(self)

        except ValidationError as e:
            cherrypy.response.status = 400
            return {"error": str(e)}

        return Service.post_service(self)

    def PUT(self):
        return Service.put_service(self)

    def DELETE(self):
        return Service.delete_service(self)
        
