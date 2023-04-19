from flask import Flask, request, make_response
from flask_cors import CORS
from flask_migrate import Migrate
from flask_restful import Api, Resource
from models import db
from butler import Client



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
        # Write image data to file
        with open('./storage/ocr_image.jpeg', 'wb') as f:
            f.write(request.data)
        
        # Make sure to first install the SDK using 'pip install butler-sdk'
 

        # Specify variables for use in script below
        api_key = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJnb29nbGUtb2F1dGgyfDEwNjkxNDc5MTMzMjAzMDMzOTY2OSIsImVtYWlsIjoibWNob2k0MTk0QGdtYWlsLmNvbSIsImVtYWlsX3ZlcmlmaWVkIjp0cnVlLCJpYXQiOjE2ODE2NjkwNzU5OTZ9.zYaCZMVgMnUWurL7CGa0JGrR29CIolKRlSvgqDZjTTU'
        queue_id = '93c11f04-c119-4f78-a7b5-036b617fda49'

        # Specify the path to the file you would like to process
        file_location = './storage/ocr_image.jpeg'

        fileinfo = Client(api_key).extract_document(queue_id, file_location)
        formFields = fileinfo.to_dict()['formFields']
        for field in formFields:
            if field['fieldName'] == "Document Number":
                license = field['value']
        # license ? 
        response = license if license else "No License found"
        return make_response(response, 200)

        # const capturedImage = async (req, res, next) => {
        # try {
        # path = './storage/ocr_image.jpeg'   
        # let imgdata = req.body.img;                 // get img as base64
        # const base64Data = imgdata.replace(/^data:([A-Za-z-+/]+);base64,/, '');     // convert base64
        # fs.writeFileSync(path, image,  {encoding: 'base64'});                  
        # Tesseract.recognize(
        #     'http://localhost:5001/img/ocr_image.jpeg',
        #     'eng',
        #     { logger: m => console.log(m) }
        # )
        # .then(({ data: { text } }) => {
        #     console.log(text)
        #     return res.send({
        #         image: imgdata,
        #         path: path,
        #         text: text
        #     });
        # })

        # } catch (e) {
        #     next(e);
        # }
    

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

