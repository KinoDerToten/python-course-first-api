from flask import Flask, jsonify

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


app.run(port=5000)
