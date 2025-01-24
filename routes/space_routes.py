from flask import Blueprint, render_template, current_app, request, flash, redirect
from lib.database_connection import get_flask_database_connection
from werkzeug.utils import secure_filename
import os
from lib.space_repository import SpaceRepository
from lib.space import Space

UPLOAD_FOLDER = os.path.join(os.getcwd(), 'static', 'img')
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

space_routes = Blueprint('space_routes', __name__)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@space_routes.route('/customer')
def customer_page():
    """
    Render the customer page with active spaces.

    Returns:
        Rendered customer.html with active spaces from the database.
    """
    connection = get_flask_database_connection(current_app)
    repository = SpaceRepository(connection)
    spaces = repository.get_all_spaces()
    
    return render_template('customer.html', spaces=spaces)

@space_routes.route('/')
def list_spaces():
    """
    Show all spaces when hitting the root route '/'

    Returns:
        Redirects to /customer showing all spaces.
    """
    return redirect('/customer')

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

@space_routes.route('/lister/<int:id>/add_space', methods=['GET'])
def load_lister_add_page(id):
    connection = get_flask_database_connection(current_app)
    repository = SpaceRepository(connection)
    spaces = repository.get_spaces_for_id(id)
    lister_id = spaces[0].lister_id
    return render_template('add_space.html', lister_id=lister_id)

@space_routes.route('/lister/<int:id>/add_space', methods=['POST'])
def add_space_lister_add_page(id):
    """
    Add a new space if the lister is logged in
    """
    connection = get_flask_database_connection(current_app)
    repository = SpaceRepository(connection)
    spaces = repository.get_spaces_for_id(id)
    lister_id = spaces[0].lister_id
    # get form data
    space_name = request.form['space-name']
    space_address = request.form['space-address']
    space_description = request.form['space-description']
    space_price = request.form['space-price']
    space_status = "Available"
    file = request.files['space-image']
    # define relative path to the image folder
    relative_path = ""
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(UPLOAD_FOLDER, filename))
        relative_path = "../static/img/" + filename
    # add a new space into database 
    repository.add_space(Space(None, space_name, space_address, space_description, space_price, id, space_status, relative_path, None, None))
    return redirect('/lister/' + str(id))
