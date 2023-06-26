import os
from flask_restful import Resource, reqparse
from flask import request
from resources.controller.get_all_files_from_zip import get_all_files_from_zip

class Unzip_files(Resource):
    
    def get(self):
        
        arquivo_zip = request.files['file']
        if not arquivo_zip:
            return {'message': 'No file found'}, 400
        
        get_all_files_from_zip(arquivo_zip)
        
        return {'message': 'Files extracted successfully'}, 200
        
