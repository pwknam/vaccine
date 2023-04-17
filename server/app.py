from flask import Flask, request, make_response
from flask_cors import CORS
from flask_migrate import Migrate
from flask_restful import Api, Resource
from models import db


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

CORS(app)
# migrate = Migrate(app, db)
# db.init(app)
api = Api(app)

class Upload(Resource):
    def post(self):
        data = request.get_json()

        # new_plant = Plant(
        #     name=data['name'],
        #     image=data['image'],
        #     price=data['price'],
        # )

        # db.session.add(new_plant)
        # db.session.commit()

        return make_response(data, 200)

api.add_resource(Upload, '/upload')

if __name__ == '__main__':
    app.run(port=5555, debug=True)

