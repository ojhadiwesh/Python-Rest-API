from flask import Flask, request
from flask_restful import Resource, Api
from flask_jwt import JWT, jwt_required

from security import authenticate, identity
from user import UserRegister
app = Flask(__name__)
app.secret_key = 'diwesh'

api = Api(app)
jwt = JWT(app, authenticate, identity)  # /auth
items =[]

class Items(Resource):
    @jwt_required()
    def get(self, name):
        item = next(filter(lambda x: x['name']==name, items ), None)
        return {'item': item}, 200 if item  else 404

    def post(self, name):
        if next(filter(lambda x: x['name']==name, items ), None) is not None:
            return {'Message': "An item with the name given  '{}' already exists".format(name)}, 400
        data= request.get_json()
        item = {'name': name, 'price' : data['price']}
        items.append(item)
        return item, 201

    def delete(self, name):
        global items
        items = list(filter(lambda x: c['name'] != name, items ))
        return {'message': 'Item deleted'}

class ItemList(Resource):
    def get(self):
        return {'items': items}


api.add_resource(Items, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(UserRegister, '/register')
app.run(port=5001, debug =True)
