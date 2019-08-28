from flask_restful import Resource
from flask import jsonify, request
from app import flaskAppInstance
import pandas as pd

# from service.LaptopServiceImpl import LaptopService
from service.HealthServiceImpl import HealthServiceImpl
class PredictController(Resource):


    def post(self):

        h = HealthServiceImpl()
        requestData = request.get_json()

        value = requestData['day']

        result = h.predict(value).tolist();

        y = result;
        print(y)

        return jsonify({"message": result});
