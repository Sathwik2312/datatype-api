from flask import Flask
from flask_restful import Api
from flask_cors import CORS
import logging

from resource.data_operations import DataTypeConversion

app = Flask(__name__)
CORS(app)
api = Api(app)

logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    filemode="a"
)

api.add_resource(DataTypeConversion, "/compare")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)