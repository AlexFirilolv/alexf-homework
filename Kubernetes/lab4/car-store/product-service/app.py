from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
import os
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize Flask application
app = Flask(__name__)

# Database configuration
DB_USER = os.getenv('DB_USER', 'root')
DB_PASSWORD = os.getenv('DB_PASSWORD', 'rootpassword')
DB_HOST = os.getenv('DB_HOST', 'mysql.database.svc.cluster.local')
DB_NAME = os.getenv('DB_NAME', 'carstore')

logger.info(f"Connecting to database at {DB_HOST}/{DB_NAME} with user {DB_USER}")

# Configure SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy with our application
db = SQLAlchemy(app)

# Model definition
class Product(db.Model):
    __tablename__ = 'products'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    brand = db.Column(db.String(255), nullable=False)
    price = db.Column(db.Float, nullable=False)
    image_url = db.Column(db.Text)
    description = db.Column(db.Text)
    specs = db.Column(db.JSON)

# Route handlers
@app.route('/test', methods=['GET'])
def test():
    return jsonify({"message": "API is working!"}), 200

@app.route('/', methods=['GET'])
def home():
    logger.info("Received request for home endpoint")
    return jsonify({
        "message": "Welcome to Premium Cars API",
        "status": "online",
        "endpoints": {
            "home": "GET /",
            "test": "GET /test",
            "list_products": "GET /products",
            "get_product": "GET /products/<id>",
            "create_product": "POST /products"
        }
    })

@app.route('/products', methods=['GET'])
def get_products():
    logger.info("Fetching all products")
    try:
        with app.app_context():
            products = Product.query.all()
            return jsonify([{
                'id': p.id,
                'name': p.name,
                'brand': p.brand,
                'price': p.price,
                'image_url': p.image_url,
                'description': p.description,
                'specs': p.specs
            } for p in products])
    except Exception as e:
        logger.error(f"Error fetching products: {str(e)}")
        return jsonify({"error": "Failed to fetch products"}), 500

if __name__ == '__main__':
    # Create tables and run the application
    with app.app_context():
        logger.info("Creating database tables...")
        db.create_all()
        logger.info("Database tables created successfully!")
    
    # Run the Flask application
    logger.info("Starting Flask application...")
    app.run(host='0.0.0.0', port=5000, debug=True)