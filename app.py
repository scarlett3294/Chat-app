from flask import Flask, render_template, redirect, url_for, request, flash, session
from flask_socketio import SocketIO, emit
from database import db, initialize_database
from model import User, Message
from helpers import is_name_registered, register_name
import os

app = Flask(__name__)

# Configure the database
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(BASE_DIR, 'family-chatroom.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'secret-key'

db.init_app(app)
socketio = SocketIO(app, cors_allowed_origins="*")

# Ensure the user is logged in to access the chatroom
@app.before_request
def ensure_logged_in():
    if 'username' not in session and request.endpoint not in ['home', 'login', 'register', 'static']:
        flash("You need to login or register first!")
        return redirect(url_for('home'))

# Create routes

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Get the username from the form
        entered_username = request.form.get('username')
        if entered_username is not None and is_name_registered(entered_username.lower()):
            session['username'] = entered_username.lower()
            return redirect(url_for('chat'))
        else:
            flash("Name not registered. Please register first.")
            return redirect(url_for('register'))
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # Get the username from the form
        username = request.form.get('username')

        # Check if the username is empty, None, or contains spaces
        if not username:
            flash("Username cannot be empty!")
        elif ' ' in username:
            flash("Username cannot contain spaces. Please choose another username.")
        elif User.query.filter_by(username=username.lower()).first():
            flash("Username already exists. Please choose another username.")
        else:
            # Register the new user with the lowercase username
            username = username.lower()
            register_name(username)
            flash("Successfully registered.")
            session['username'] = username

            return redirect(url_for('chat'))

    return render_template('register.html')


@app.route('/chat')
def chat():
    # Get the username to display the name of the user logged in
    username = session.get('username')
    # Fetch the last 100 messages from the database
    recent_messages = Message.query.order_by(Message.timestamp.desc()).limit(100).all()
    return render_template('chat.html', recent_messages=recent_messages, username=username)

@app.route('/logout')
def logout():
    session.pop('username', None)  # Remove the user from the session
    flash("You've been logged out!")
    return redirect(url_for('home'))

# Integrate Flask-SocketIO

@socketio.on('send_message')
def handle_message(data):
    # Save the message to the database
    new_message = Message()
    new_message.content = data['message']
    user = User.query.filter_by(username=session['username']).first()
    if user:
        new_message.user_id = user.id
    else:
        flash("User not found.")
        return redirect(url_for('home'))
    db.session.add(new_message)
    db.session.commit()

    # Format the time for display
    formatted_timestamp = new_message.timestamp.strftime('%Y-%m-%d %H:%M')

    # Broadcast the message to all connected members
    emit('receive_message', {'message': data['message'], 'user_id': session['username'], 'timestamp': formatted_timestamp}, broadcast=True)

if __name__ == '__main__':
    initialize_database(app)
    socketio.run(app, host='0.0.0.0', use_reloader=True, log_output=True)

