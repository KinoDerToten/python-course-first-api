from flask import Flask, jsonify, request

app = Flask(__name__)

purchase_orders = [
    {
        'id': 1,
        'description': 'Pedido de compras',
        'items': [
            {
                'id': 1,
                'description': 'Item do pedido 1',
                'price': 20.99
            }
        ]
    },
    {
        'id': 2,
        'description': 'Pedido de compras',
        'items': [
            {
                'id': 3,
                'description': 'Item do pedido 2',
                'price': 20.99
            }
        ]
    },
    {
        'id': 3,
        'description': 'Pedido de compras',
        'items': [
            {
                'id': 3,
                'description': 'Item do pedido 3',
                'price': 20.99
            }
        ]
    }
]


@app.route('/')
def home():
    return "Hello World"


@app.route('/purchase_orders')
def get_purchase_orders():
    return jsonify(purchase_orders)


@app.route('/purchase_orders/<int:id>')
def get_purchase_orders_by_id(id):
    for po in purchase_orders:
        if po['id'] == id:
            return jsonify(po)
    return jsonify({'message': 'Pedido {} não encontrado'.format(id)})


@app.route('/purchase_orders', methods=['POST'])
def create_purchase_order():
    request_data = request.get_json()
    purchase_order = {
        'id': request_data['id'],
        'description': request_data['description'],
        'items': []
    }
    purchase_orders.append(purchase_order)
    return jsonify(purchase_order)


@app.route('/purchase_orders/<int:id>/items')
def get_purchase_orders_items(id):
    for po in purchase_orders:
        return jsonify(po['items'])


@app.route('/purchase_orders/<int:id>/items', methods=['POST'])
def create_purchase_orders_items(id):
    req_data = request.get_json()
    for po in purchase_orders:
        po['items'].append(
            {
                'id': req_data['id'],
                'description': req_data['description'],
                'price': req_data['price']
            }
        )
        return jsonify(po)
    return jsonify({'message': 'Pedido {} não encontrado'.format(id)})


app.run(port=5000)
