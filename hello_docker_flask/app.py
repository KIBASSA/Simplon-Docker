# app.py - a minimal flask api using flask_restful
from flask import Flask
from flask_restful import Resource, Api,reqparse

app = Flask(__name__)
api = Api(app)

# Define parser and request args
parser = reqparse.RequestParser()
parser.add_argument('x', type=float, default=False, required=False)
parser.add_argument('y', type=float, default=False, required=False)

class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

class Multiply(Resource):
    def get(self, x):
        result = x * x
        return {'result':result}

    def post(self,x):
        result = x * x
        return {"result":result}, 200

class Add(Resource):
    def get(self):
        args = parser.parse_args()
        x = args['x']  
        y = args['y'] 
        result = float(x) + float(y)
        return {"result":result}
    
    def post(self):
        args = parser.parse_args()
        x = args['x']  
        y = args['y'] 
        result = float(x) + float(y)
        return {"result":result}, 200

api.add_resource(HelloWorld, '/hello')
api.add_resource(Multiply, '/multiply/<float:x>')
api.add_resource(Add, '/add')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')