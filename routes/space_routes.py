from flask import Blueprint, render_template, current_app
from lib.database_connection import get_flask_database_connection

space_routes = Blueprint('space_routes', __name__)

@space_routes.route('/customer')
def customer_page():
    """
    Render the customer page with active spaces.

    Returns:
        Rendered customer.html with active spaces from the database.
    """
    connection = get_flask_database_connection(current_app)
    spaces = connection.execute(
        "SELECT space_id, space_name, space_description, space_price FROM spaces WHERE space_active = TRUE;"
    )
    return render_template('customer.html', spaces=spaces)


@space_routes.route('/lister')
def lister_page():
    """
    Render the lister page with all spaces.

    Returns:
        Rendered lister.html with all spaces from the database.
    """
    connection = get_flask_database_connection(current_app)
    spaces = connection.execute(
        "SELECT space_id, space_name, space_description, space_price FROM spaces;"
    )
    return render_template('lister.html', spaces=spaces)
