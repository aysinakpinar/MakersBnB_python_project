from flask import Blueprint, render_template, current_app, request
from lib.database_connection import get_flask_database_connection
from lib.space_repository import SpaceRepository

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
        "SELECT space_id, space_name, space_description, space_price FROM spaces"
    )
    return render_template('customer.html', spaces=spaces)


@space_routes.route('/lister/<int:id>', methods=['GET'])
def lister_page(id):
    """
    Render the lister page with all spaces.

    Returns:
        Rendered lister.html with all spaces from the database.
    """
    connection = get_flask_database_connection(current_app)
    repository = SpaceRepository(connection)
    spaces = repository.get_spaces_for_id(id)
    return render_template('lister.html', spaces=spaces, current_status="All")

@space_routes.route('/lister/<int:id>', methods=['POST'])
def lister_page_update(id):
    """
    Render the lister page with specific status of spaces.
    """
    connection = get_flask_database_connection(current_app)
    repository = SpaceRepository(connection)
    status = request.form['status']
    if status == "All":
        spaces = repository.get_spaces_for_id(id)
    else:
        spaces = repository.get_spaces_by_id_and_status(id, status)
    return render_template('lister.html', spaces=spaces, current_status=status)