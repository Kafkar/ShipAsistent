from flask import Flask
from routes import register_blueprints
from logger import Logger


app = Flask(__name__)
logger = Logger(app)

# Register blueprints
register_blueprints(app)

if __name__ == '__main__':
    app.run(debug=True)
