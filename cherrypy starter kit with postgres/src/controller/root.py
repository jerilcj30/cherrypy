import cherrypy
import cherrypy_cors
import os


__all__ = ["Root"]

"""
  Storing the tree recieved in the database
  
  1. Create a Materialized View which has results of the below query
  2. The below query is a recursive SQL Query => https://www.youtube.com/watch?v=7hZYh9qXxe4

 with recursive main_tree as 
   (select id, node, parent, node_type, url, weight, 1 as lvl
    from campaigns where parent = 'jose'
    union
    select E.id, E.node, E.parent, E.node_type, E.url, E.weight, H.lvl+1 as lvl
    from main_tree H 
    join campaigns E on H.node = E.parent    
   )
select * from main_tree;   

"""


class Root(object):
    def __init__(self):
        pass

    @cherrypy.expose
    @cherrypy.tools.json_in()
    @cherrypy.tools.json_out()
    def index(self):        
        return "Hello"
