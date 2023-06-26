from flask import Flask
from flask_restful import  Api


app = Flask(__name__)
app.config.from_object('config.DevelopmentConfig')
# observer = Observer()


api = Api(app)

@app.route('/')
def home():
    return 'Hello World!'

from resources.file_handler import Unzip_files
api.add_resource(Unzip_files, '/unzip')

if __name__ == '__main__':
    
    app.run(debug=True, port=5002)