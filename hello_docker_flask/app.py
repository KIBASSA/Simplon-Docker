# app.py - a minimal flask api using flask_restful
from flask import Flask
from flask_restful import Resource, Api,reqparse

app = Flask(__name__)
api = Api(app)

# Define parser and request args
parser = reqparse.RequestParser()
parser.add_argument('x', type=int, default=False, required=False)
parser.add_argument('y', type=int, default=False, required=False)

class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

class Multiply(Resource):
    def get(self, x):
        result = x * x
        return {'result':result}

class Add(Resource):
    def get(self):
        args = parser.parse_args()
        x = args['x']  
        y = args['y'] 
        #api.add_resource(Add, '/add/?x=<int:x>&y=<int:y>')
        result = int(x) + int(y)
        return {"result":result}

    #def post(self):
    #    args = parser.parse_args()
    #    todo_id = int(max(TODOS.keys()).lstrip('todo')) + 1
    #    todo_id = 'todo%i' % todo_id
    #    TODOS[todo_id] = {'task': args['task']}
     #   return TODOS[todo_id], 201

api.add_resource(HelloWorld, '/hello')
api.add_resource(Multiply, '/multiply/<int:x>')
#api.add_resource(Add, '/add/?x=<int:x>&y=<int:y>')
api.add_resource(Add, '/add')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')