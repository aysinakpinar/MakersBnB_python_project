import os
from dotenv import load_dotenv
from flask import Flask, request, render_template, session
from lib.database_connection import get_flask_database_connection
from routes.space_routes import space_routes
from routes.auth_routes import auth_routes
from routes.info_routes import info_routes

#load local env vars
load_dotenv()

# Create a new Flask app
app = Flask(__name__, static_folder='static')
app.register_blueprint(space_routes)
app.register_blueprint(auth_routes)
app.register_blueprint(info_routes)

#load secret key for sessions to app from .env
app.secret_key = os.getenv('SECRET_KEY', 'default_secret_key')  # Fallback if not set
@app.context_processor
def inject_user():
    return {
        'logged_in': session.get('logged_in', False),
        'user_role': session.get('user_role', None)
    }


# == Your Routes Here ==

# GET /index
# Returns the homepage
# Try it:
#   ; open http://localhost:5001/index
@app.route('/index', methods=['GET'])
def get_index():
    return render_template('index.html')

# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))
