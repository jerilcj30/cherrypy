import cherrypy
import cherrypy_cors
from src.models.model import Campaign as ModelCampaign

# from models.campaign import Campaign as ModelCampaign
from sqlalchemy.exc import SQLAlchemyError

__all__ = ["Campaigns"]

""" This route returns all the campaigns created in the campaigns table

To call this route http://localhost/api/campaigns/

"""


class Campaigns(object):
    def __init__(self):
        pass

    @property
    def db(self):
        return cherrypy.request.db

    # Define a new method to handle querying the database
    def query_database(self):
        results = []
        try:
            # Query the database for the campaigns
            results = (
                self.db.query(
                    ModelCampaign.campaign_id,
                    ModelCampaign.node,
                    ModelCampaign.budget,
                    ModelCampaign.cpc,
                    ModelCampaign.traffic_Source,
                )
                .filter(ModelCampaign.parent == "CAMPAIGN")
                .all()
            )

        except SQLAlchemyError as error:
            print(error)
            return {"error": "Error querying database"}

        return results

    @cherrypy.expose
    @cherrypy.tools.json_in()
    @cherrypy.tools.json_out()
    def index(self):

        if cherrypy.request.method == "OPTIONS":
            cherrypy_cors.preflight(allowed_methods=["GET"])

        if cherrypy.request.method == "GET":
            results = self.query_database()  # Call the query_database method

            # Convert the query results into a list of dictionaries
            response = [row._asdict() for row in results]

        return response
