from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
app = Flask(__name__)
 
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.config['SECRET_KEY'] = '0bf4e4cb188288bd1303d6d6'
db = SQLAlchemy(app)

bcrypt = Bcrypt(app)

login_manager = LoginManager(app)
login_manager.login_view = "login_page"
login_manager.login_message = "Please log in first to access market"
login_manager.login_message_category = "info"

from market import routes


# @app.route('/login', methods=['GET', 'POST'])
# def login_page():
#     form = LoginForm()
#     if form.validate_on_submit():
#         attempted_user = User.query.filter_by(username=form.username.data).first()
#         if attempted_user and attempted_user.check_password_correction(
#                 attempted_password=form.password.data
#         ):
#             login_user(attempted_user)
#             flash(f'Success! You are logged in as: {attempted_user.username}', category='success')
#             return redirect(url_for('market_page'))
#         else:
#             flash('Username and password are not match! Please try again', category='danger')

#     return render_template('login.html', form=form)
