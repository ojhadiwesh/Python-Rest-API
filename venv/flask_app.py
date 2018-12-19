from flask import Flask, jsonify, request

app= Flask(__name__)

stores = [

    {
        'name': 'amazon',
        'items':[
            {
            'name': 'My Item',
            'price': 16
            }
        ]
    }
]



@app.route('/store', methods =['POST'] ) # http://localhost:5001/

def create_store():
    request_data = request.get_json()
    new_store= {
        'name': request_data['name'],
        'items': []
    }
    stores.append(new_store)
    return jsonify({'stores': stores})

@app.route('/store/<string:name>')

def get_store(name):
    for store in stores:
        if store['name']==name:
            return jsonify(store)
    return jsonify('There was no store of that name')


@app.route('/store/<string:name>/item', methods =['POST'])

def create_item_in_store(name):
    pass

@app.route('/stores')

def get_stores():
    return response.json({'stores': stores})

app.run(port = '5001')
