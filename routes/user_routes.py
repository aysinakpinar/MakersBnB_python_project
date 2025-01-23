from flask import Blueprint, request, render_template, redirect, current_app, session
from lib.database_connection import get_flask_database_connection
from lib.user import User
from lib.user_repository import UserRepository


user_routes = Blueprint('user_routes', __name__)

# Edit user details (GET)
@user_routes.route('/user_details', methods=['GET'])
def get_user_details():
    if not session.get('user_email'):
        return redirect('/login')
    user_email = session.get('user_email')
    if not user_email:
        return redirect('/login')  # Redirect if email is not in the session
    """
    Render the user details page.

    Returns:
        A rendered HTML template for the user details
    """
    connection = get_flask_database_connection(current_app)
    repository = UserRepository(connection)
    user = repository.find(user_email)
    return render_template('user_details.html', user = user)  # gets user details

# Edit user details (POST)
@user_routes.route('/edit_username', methods=['POST'], endpoint='post_edit_username')
def post_edit_username():
    """

        Updates the username in the database based on the form data.

    Returns:
        Redirect to the user_details page after updating.
    """

    connection = get_flask_database_connection(current_app)
    repository = UserRepository(connection)
    new_username = request.form['new_user_username']
    user_email = request.form.get('user_email')
    repository.update_username(user_email, new_username)
    return redirect('/user_details')

@user_routes.route('/edit_password', methods=['POST'], endpoint='post_edit_password')
def post_edit_password():
    """

        Updates the password/password_hash in the database based on the form data.

    Returns:
        Redirect to the user_details page after updating.
    """

    connection = get_flask_database_connection(current_app)
    repository = UserRepository(connection)
    new_user_password = request.form['new_user_user_password']
    user_email = request.form['user_email']
    repository.update_user_password(user_email, new_user_password)
    return redirect('/user_details')

@user_routes.route('/edit_email', methods=['POST'], endpoint='post_edit_email')
def post_edit_email():
    """

        Updates the email in the database based on the form data.

    Returns:
        Redirect to the user_details page after updating.
    """
    connection = get_flask_database_connection(current_app)
    repository = UserRepository(connection)
    new_user_email = request.form['new_user_email']
    user_email = request.form['user_email']
    repository.update_user_email(user_email, new_user_email)
    return redirect('/user_details')

@user_routes.route('/delete_account', methods=['DELETE'], endpoint='delete_account')
def delete_account():
    """

        Updates the email in the database based on the form data.

    Returns:
        Redirect to the user_details page after updating.
    """
    connection = get_flask_database_connection(current_app)
    repository = UserRepository(connection)
    user_email = request.form['user_email']
    repository.delete_account(user_email)
    return "Account was successfully deleted"


@user_routes.route('/logout', methods=['GET'])
def logout():
    """
    Redirect to the logout splash page.
    """
    return redirect('/logout_page')  # Redirect to the logout splash page

@user_routes.route('/logout_page', methods=['GET'])
def logout_page():
    """
    Render the logout page with a countdown.
    Clears the session data and displays a splash screen with a countdown
    before redirecting to the index page.
    """
    session.clear()  # Clear session data
    return render_template('logout.html')

@user_routes.route('/index', methods=['GET'])
def index():
    """
    Render the login page or redirect logged-in users.

    If the user is already logged in, redirect them to the customer dashboard.
    Otherwise, display the login form.

    Returns:
        Redirect to the customer dashboard if logged in.
        Rendered HTML template for the login form if not logged in.
    """
    if session.get('logged_in'):  # Check if the user is logged in
        return redirect('/customer')  # Redirect to "Browse Spaces" page
    return render_template('index.html')  # Render login form if not logged in
