#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
from dotenv import load_dotenv
import cherrypy
import tempfile
import src.controller.root.index
from models.model import ORBase
from cp_sqlalchemy import SQLAlchemyTool, SQLAlchemyPlugin
from plugins.cp_redis.redis_plugin import RedisPlugin
from plugins.cp_redis.redis_tool import RedisTool

class Server(object):
    def __init__(self):

        # Get the path to the .env file
        env_path_dev = os.path.join(os.path.dirname(__file__), '..', '.env')
        
        if os.path.exists('/.dockerenv'):
            print("Inside Docker")
        else:
            # Load variables from .env file
            load_dotenv(env_path_dev)

        self._set_basic_config()
        self._setup()
        self._add_app()
       
    def _set_basic_config(self):
        self.base_dir = os.path.dirname(os.path.abspath(__file__))
        self.conf_path = os.path.join(self.base_dir, "conf")
        log_dir = os.path.join(self.base_dir, "./logs")
        if not os.path.exists(log_dir):
            os.mkdir(log_dir)
        session_dir = os.path.join(tempfile.gettempdir(), "sessions")
        if not os.path.exists(session_dir):
            os.mkdir(session_dir)

    def _setup(self):

        # Update the global settings for the HTTP server and engine
        cherrypy.config.update(os.path.join(self.conf_path, "server.conf"))

    def _add_app(self):

        cherrypy.tree.mount(
            src.controller.root.index.Root(),
            "/api",
            os.path.join(self.conf_path, "app.conf"),
        )   
        

    def run(self):
        engine = cherrypy.engine

        cherrypy.tools.db = SQLAlchemyTool()
        cherrypy.tools.rdb = RedisTool()

        sqlalchemy_plugin = SQLAlchemyPlugin(
            engine, ORBase, os.getenv("DATABASE_URL") , echo=True
        )

        redis_plugin = RedisPlugin(engine, os.getenv("REDIS_HOST"), os.getenv("REDIS_PORT"), os.getenv("REDIS_DB"))

        if hasattr(engine, "signal_handler"):
            engine.signal_handler.subscribe()

        if hasattr(engine, "console_control_handler"):
            engine.console_control_handler.subscribe()

        sqlalchemy_plugin.subscribe()
        sqlalchemy_plugin.create()

        redis_plugin.subscribe()       

        engine.start()
        engine.block()


if __name__ == "__main__":
    Server().run()
