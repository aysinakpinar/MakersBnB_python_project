from flask import Blueprint, request, render_template, redirect, current_app, session, flash
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
    new_username = request.form.get('new_username')
    user_email = session.get('user_email')

    if not user_email:
        # Redirect to login page if session doesn't contain the email
        return redirect('/login')
    try:
        # Update the username in the database
        repository.update_username(user_email, new_username)
    finally:
        flash('Username updated successfully.', 'success')
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
    new_user_password = request.form['new_password']
    user_email = session.get('user_email')

    if not user_email:
        # Redirect to login page if session doesn't contain the email
        return redirect('/login')
    try:
        # Update the password in the database
        repository.update_user_password(user_email, new_user_password)
    finally:
        flash('Password updated successfully.', 'success')
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
    new_user_email = request.form.get('new_email')
    user_email = session.get('user_email')

    if not user_email:
        # Redirect to login page if session doesn't contain the email
        return redirect('/login')
    try:
        # Update the password in the database
        repository.update_user_email(user_email, new_user_email)
    finally:
        flash('Email updated successfully. Returning to log in page', 'success')
        session.clear()
    return redirect('/index')

@user_routes.route('/delete_account', methods=['POST'], endpoint='delete_account')
def delete_account():
    """

        Deletes the account

    Returns:
        Redirect to the homepage
    """
    connection = get_flask_database_connection(current_app)
    repository = UserRepository(connection)
    user_email = session.get('user_email')

    if not user_email:
        # Redirect to login page if session doesn't contain the email
        return redirect('/login')
    try:
        # Update the password in the database
        repository.delete_account(user_email)
    finally:
        flash('Account was successfully deleted', 'success')
        session.clear()
    return redirect('/login')


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
