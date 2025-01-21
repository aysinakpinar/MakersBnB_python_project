from flask import Blueprint, render_template
from lib.database_connection import get_flask_database_connection

info_routes = Blueprint('info_routes', __name__)

@info_routes.route('/about', methods=['GET'])
def about():
    """
    Render the About Us page.

    Serves the static "About Us" page to provide information
    about the MakersBnB platform.

    Returns:
        A rendered HTML template for the About Us page.
    """
    return render_template('about.html')
