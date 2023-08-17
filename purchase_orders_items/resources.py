from flask import jsonify
from flask_restful import Resource
from purchase_orders.resources import purchase_orders


class PurchaseOrdersItems(Resource):
    def get(self, id):
        for po in purchase_orders:
            if po['id'] == id:
                return jsonify(po['items'])
        return {'message': f'Pedido {id} não encontrado'}
