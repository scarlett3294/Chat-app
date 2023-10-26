# Family CHATroom

#### Video Demo:  <https://youtu.be/HOBx3lGwSq4>

#### Description: Family CHATroom is a user-friendly web application designed exclusively for family members. It provides a convenient and secure platform for family members to stay connected, share updates, and communicate effortlessly. Leveraging a stack of powerful technologies including HTML, Jinja2 templating, JavaScript, Python, Flask for web development, Flask-SQLAlchemy for robust database management, and Flask-SocketIO for real-time messaging, this app offers a seamless and interactive family chat experience.
## File Structure
- **app.py**: This is the main application file where the Flask web application is defined. It handles routing, authentication, and real-time messaging functionality.
- **helpers.py**: This file contains helper functions related to user registration and checking if a username is already registered.
- **model.py**: This file defines the data models for the application using SQLAlchemy. It defines two models: User and Message.
- **database.py**: This file is responsible for initializing the database using Flask-SQLAlchemy. It sets up the SQLAlchemy object db and provides a function initialize_database(app) to create the necessary database tables.
- **templates**: This folder contains HTML templates used to render the web pages.

## Design Choices
I chose to implement a name-based login system to prioritize ease of use, especially for family members who may not be tech-savvy. This eliminates the need for complex usernames and passwords, simplifying the login process.

#### Installation:
  Before you begin, make sure you have Python 3.7 or higher installed.
  I recommend using a virtual environment to isolate your project's dependencies.
  Here's how to set up a virtual environment and install the required packages:
#### 1. Create a virtual environment (optional but recommended):
  If you're using venv: python -m venv venv
  If you're using virtualenv: virtualenv venv
#### 2. Activate the virtual environment:
  On Windows: venv\Scripts\activate
  On macOS and Linux: source venv/bin/activate
#### 3. Install project dependencies: pip install -r requirements.txt
#### 4. To initialize database run: python app.py
#### 5. To run the app for real-time messaging, use the following command: flask run --host=0.0.0.0
  This command enables real-time messaging across different devices.
#### Visit http://< your-ip >:5000 in your web browser to access the application (computer/ phone)
#### Replace < your-ip > with your server's IP address.
#### To deactivate the virtual environment when you're done, simply run: deactivate
