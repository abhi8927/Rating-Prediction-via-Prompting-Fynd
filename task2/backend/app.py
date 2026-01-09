"""
Main Flask application.
Sets up the API server with CORS, routes, and database initialization.
"""

from flask import Flask
from flask_cors import CORS
from models import init_database
from routes.reviews import init_reviews_routes
from routes.admin import init_admin_routes
import os

app = Flask(__name__)
CORS(app)

# Initialize database
db_session_factory = init_database()

# Initialize routes
init_reviews_routes(app, db_session_factory)
init_admin_routes(app, db_session_factory)


@app.route('/api/health', methods=['GET'])
def health_check():
    """
    Health check endpoint.
    """
    return {"status": "ok", "message": "API is running"}, 200


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
