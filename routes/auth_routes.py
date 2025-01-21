from flask import Blueprint, request, render_template, redirect, current_app, session
from lib.database_connection import get_flask_database_connection

auth_routes = Blueprint('auth_routes', __name__)

# Sign-Up Form (GET)
@auth_routes.route('/signup', methods=['GET'], endpoint='get_signup')
def get_signup():
    """
    Render the signup form page.

    Returns:
        A rendered HTML template for the signup form.
    """
    return render_template('signup.html')  # Serves the signup form

# Sign-Up Submission (POST)
@auth_routes.route('/signup', methods=['POST'], endpoint='post_signup')
def post_signup():
    """
    Handle signup form submission.

    Inserts a new user into the database based on the form data and redirects
    to the login page.

    Returns:
        Redirect to the login page after successful signup.
    """
    connection = get_flask_database_connection(current_app)
    data = request.form
    connection.execute(
        "INSERT INTO user_details (user_username, user_password, user_email, user_role) VALUES (%s, %s, %s, %s)",
        [data['username'], data['password'], data['email'], data['role']]
    )
    return redirect('/index')

# Login Page (GET)
@auth_routes.route('/login', methods=['GET'])
def get_login():
    """
    Render the login form page.

    Returns:
        A rendered HTML template for the login form.
    """
    return render_template('index.html')  # index.html now contains the login form

@auth_routes.route('/login', methods=['POST'])
def post_login():
    """
    Handle login form submission.

    Validates user credentials from the database and stores session data for
    the logged-in user. Redirects to either the customer or lister page based
    on the user's role.

    Returns:
        Redirect to the appropriate dashboard page if login is successful.
        HTTP 401 with an error message if login fails.
    """
    connection = get_flask_database_connection(current_app)
    data = request.form

    # Query the user from the database
    user = connection.execute(
        "SELECT * FROM user_details WHERE user_email = %s AND user_password = %s",
        [data['email'], data['password']]
    )

    if user:
        user = user[0]  # Fetch the first result
        session['logged_in'] = True
        session['user_role'] = user['user_role']  # 'customer' or 'lister'
        session['user_email'] = user['user_email']
        return redirect('/customer' if user['user_role'] == 'customer' else '/lister')

    return "Invalid email or password", 401

@auth_routes.route('/logout', methods=['GET'])
def logout():
    """
    Redirect to the logout splash page.
    """
    return redirect('/logout_page')  # Redirect to the logout splash page

@auth_routes.route('/logout_page', methods=['GET'])
def logout_page():
    """
    Render the logout page with a countdown.
    Clears the session data and displays a splash screen with a countdown
    before redirecting to the index page.
    """
    session.clear()  # Clear session data
    return render_template('logout.html')

@auth_routes.route('/index', methods=['GET'])
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
