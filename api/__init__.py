from flask_restful import Api


from app import flaskAppInstance
from .PredictController import PredictController

restServer = Api(flaskAppInstance)

restServer.add_resource(PredictController, "/api-health")