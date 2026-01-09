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
from dotenv import load_dotenv

# Load environment variables from .env file
env_path = os.path.join(os.path.dirname(__file__), '.env')
if os.path.exists(env_path):
    load_dotenv(env_path)
else:
    # Fallback: try loading from current directory
    load_dotenv()

# Set API key if not found (for testing)
if not os.getenv('GEMINI_API_KEY'):
    # Try reading from .env file manually
    try:
        with open(env_path, 'r', encoding='utf-8') as f:
            for line in f:
                if line.startswith('GEMINI_API_KEY='):
                    os.environ['GEMINI_API_KEY'] = line.split('=', 1)[1].strip()
                    break
    except Exception as e:
        pass
    
    # Fallback: set directly if still not found
    if not os.getenv('GEMINI_API_KEY'):
        os.environ['GEMINI_API_KEY'] = 'AIzaSyDnfybUacyg2A4WqPR7GjhuLVY00r18xh4'

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
    app.run(host='0.0.0.0', port=port, debug=False)
