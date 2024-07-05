from flask import Flask, request, jsonify
from flask_restful import Api, Resource
from flask_mongoengine import MongoEngine
from flask_admin import Admin
from flask_admin.contrib.mongoengine import ModelView

app = Flask(__name__)
api = Api(app)

# Database configuration
app.config['MONGODB_SETTINGS'] = {
    'db': 'kralov_kava',
    'host': 'localhost',
    'port': 27017
}

db = MongoEngine()
db.init_app(app)

# Define the Product model
class Product(db.Document):
    name = db.StringField(required=True)
    price = db.FloatField(required=True)
    description = db.StringField()
    imageUrl = db.StringField()

# Flask-Admin configuration
admin = Admin(app, name='Kralov KAVA Admin', template_mode='bootstrap3')
admin.add_view(ModelView(Product))

# Define the Product Resource
class ProductResource(Resource):
    def get(self, product_id=None):
        if product_id:
            product = Product.objects(id=product_id).first()
            if not product:
                return {'error': 'Product not found'}, 404
            return jsonify(product.to_json())
        products = Product.objects()
        return jsonify([product.to_json() for product in products])

    def post(self):
        data = request.get_json()
        product = Product(**data).save()
        return jsonify(product.to_json()), 201

    def put(self, product_id):
        data = request.get_json()
        product = Product.objects(id=product_id).update_one(**data)
        if not product:
            return {'error': 'Product not found'}, 404
        product = Product.objects(id=product_id).first()
        return jsonify(product.to_json())

    def delete(self, product_id):
        product = Product.objects(id=product_id).first()
        if not product:
            return {'error': 'Product not found'}, 404
        product.delete()
        return '', 204

# Add resource routes
api.add_resource(ProductResource, '/api/products', '/api/products/<product_id>')

if __name__ == '__main__':
    app.run(debug=True, port=5000)

