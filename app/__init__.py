from flask import Flask
from app.database import db
from app.routes import api_blueprint
import os

app = Flask(__name__)

# Update the database connection configuration
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://cdr:123456@localhost:5432/user_data'

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://cdr:123456@192.168.0.10:5432/user_data'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db.init_app(app)

# Register the blueprint
app.register_blueprint(api_blueprint)

# Create the database tables
with app.app_context():
    db.create_all()

# Run the Application
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
